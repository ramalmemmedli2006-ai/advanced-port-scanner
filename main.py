from scanner.cli import build_parser
from scanner.ports import parse_ports
from scanner.resolver import resolve_target
from scanner.scanner import PortScanner
from scanner.utils import print_results, export_json


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    target_host, target_ip = resolve_target(args.target)

    ports = parse_ports(args.ports)
    scanner = PortScanner(
        target_host=target_host,
        target_ip=target_ip,
        ports=ports,
        timeout=args.timeout,
        threads=args.threads,
        banner_limit=args.banner_limit,
    )

    results = scanner.run()

    print_results(
        target_host=target_host,
        target_ip=target_ip,
        total_ports=len(ports),
        results=results,
    )

    if args.json:
        export_json(args.json, target_host, target_ip, results)
        print(f"\n[OK] Results exported to {args.json}")


if __name__ == "__main__":
    main()
