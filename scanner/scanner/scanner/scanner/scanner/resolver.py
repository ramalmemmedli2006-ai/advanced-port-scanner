import socket


def resolve_target(target: str) -> tuple[str, str]:
    try:
        ip_address = socket.gethostbyname(target)
        return target, ip_address
    except socket.gaierror as error:
        raise ValueError(f"Failed to resolve target '{target}': {error}") from error
