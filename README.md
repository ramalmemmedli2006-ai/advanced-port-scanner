# Advanced Port Scanner

A professional multithreaded Python port scanner for network reconnaissance and security analysis.

## Author
Ramal Memmedli  
IT Student | Network | Cybersecurity | Helpdesk | System Administration

---

## Overview

Advanced Port Scanner is a Python-based CLI tool that scans TCP ports on a target host, identifies open ports, attempts banner grabbing, maps common services, and exports results in a structured format.

This project is designed for:
- Cybersecurity learning
- Network reconnaissance
- Service discovery
- Building a strong GitHub portfolio
- Practicing Python and socket programming

---

## Features

- Multithreaded TCP port scanning
- Custom port ranges
- Hostname to IP resolution
- Common service detection
- Banner grabbing
- Timeout control
- JSON result export
- Clean CLI interface
- Structured and modular codebase

---

## Tech Stack

- Python
- socket
- concurrent.futures
- argparse
- json
- dataclasses

---

## Project Structure

```text
advanced-port-scanner/
├── README.md
├── requirements.txt
├── main.py
├── scanner/
│   ├── cli.py
│   ├── models.py
│   ├── ports.py
│   ├── resolver.py
│   ├── scanner.py
│   ├── services.py
│   └── utils.py
├── output/
└── tests/
