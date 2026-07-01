from dataclasses import dataclass, field


@dataclass
class ServiceConfig:
    name: str
    enabled: bool = True
    autostart: bool = False
    depends_on: list[str] = field(default_factory=list)