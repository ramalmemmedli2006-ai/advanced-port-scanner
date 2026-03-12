from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ScanResult:
    port: int
    status: str
    service: str
    banner: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)
