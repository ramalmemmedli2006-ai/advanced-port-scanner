import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Advanced multithreaded TCP port scanner"
    )

    parser.add_argument(
        "target",
        help="Target hostname or IP address",
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Port range or list (example: 1-1024 or 22,80,443)",
    )

    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=100,
        help="Number of worker threads",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=0.8,
        help="Socket timeout in seconds",
    )

    parser.add_argument(
        "--banner-limit",
        type=int,
        default=1024,
        help="Maximum banner bytes to read",
    )

    parser.add_argument(
        "--json",
        help="Export scan results to JSON file",
    )

    return parser
