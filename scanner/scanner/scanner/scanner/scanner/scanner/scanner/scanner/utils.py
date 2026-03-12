import json
from datetime import datetime
from pathlib import Path

from scanner.models import ScanResult


def print_results(
    target_host: str,
    target_ip: str,
    total_ports: int,
    results: list[ScanResult],
) -> None:
    print("=" * 60)
    print("ADVANCED PORT SCANNER")
    print("=" * 60)
    print(f"Target       : {target_host}")
    print(f"Resolved IP  : {target_ip}")
    print(f"Ports Scanned: {total_ports}")
    print(f"Open Ports   : {len(results)}")

    if not results:
        print("\nNo open ports found.")
        return

    print("\nOPEN PORTS")
    print("-" * 60)
    for item in results:
        banner = item.banner if item.banner else "-"
        print(f"{item.port:<10}{item.service:<15}{banner}")


def export_json(
    file_path: str,
    target_host: str,
    target_ip: str,
    results: list[ScanResult],
) -> None:
    output_file = Path(file_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "target_host": target_host,
        "target_ip": target_ip,
        "scanned_at": datetime.utcnow().isoformat() + "Z",
        "open_ports": [result.to_dict() for result in results],
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
