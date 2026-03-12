import concurrent.futures
import socket

from scanner.models import ScanResult
from scanner.services import get_service_name


class PortScanner:
    def __init__(
        self,
        target_host: str,
        target_ip: str,
        ports: list[int],
        timeout: float = 0.8,
        threads: int = 100,
        banner_limit: int = 1024,
    ) -> None:
        self.target_host = target_host
        self.target_ip = target_ip
        self.ports = ports
        self.timeout = timeout
        self.threads = threads
        self.banner_limit = banner_limit

    def _grab_banner(self, sock: socket.socket, port: int) -> str | None:
        try:
            if port in (80, 8080, 8000, 8888):
                sock.sendall(
                    f"HEAD / HTTP/1.0\r\nHost: {self.target_host}\r\n\r\n".encode()
                )
            elif port in (21, 22, 25, 110, 143):
                pass
            else:
                try:
                    sock.sendall(b"\r\n")
                except OSError:
                    return None

            data = sock.recv(self.banner_limit)
            banner = data.decode("utf-8", errors="replace").strip()
            return banner if banner else None
        except OSError:
            return None

    def _scan_port(self, port: int) -> ScanResult | None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)

        try:
            result = sock.connect_ex((self.target_ip, port))
            if result != 0:
                return None

            service = get_service_name(port)
            banner = self._grab_banner(sock, port)

            return ScanResult(
                port=port,
                status="open",
                service=service,
                banner=banner,
            )
        except OSError:
            return None
        finally:
            sock.close()

    def run(self) -> list[ScanResult]:
        open_results: list[ScanResult] = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self._scan_port, port): port for port in self.ports}

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result is not None:
                    open_results.append(result)

        open_results.sort(key=lambda item: item.port)
        return open_results
