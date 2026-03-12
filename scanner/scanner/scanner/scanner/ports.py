def parse_ports(port_expression: str) -> list[int]:
    port_expression = port_expression.strip()
    ports = set()

    for part in port_expression.split(","):
        part = part.strip()

        if not part:
            continue

        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start = int(start_str)
            end = int(end_str)

            if start < 1 or end > 65535 or start > end:
                raise ValueError(f"Invalid port range: {part}")

            ports.update(range(start, end + 1))
        else:
            port = int(part)
            if port < 1 or port > 65535:
                raise ValueError(f"Invalid port: {port}")
            ports.add(port)

    if not ports:
        raise ValueError("No valid ports provided")

    return sorted(ports)
