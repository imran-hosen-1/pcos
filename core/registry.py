from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, Optional


@dataclass
class ServiceConfig:
    name: str
    type: str
    start: str
    stop: str
    autostart: bool = False
    metadata: Dict[str, Any] | None = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "start": self.start,
            "stop": self.stop,
            "autostart": self.autostart,
            **(self.metadata or {}),
        }


class Registry:
    def __init__(self, path: Path | str) -> None:
        self.path = Path(path)
        self._services: Dict[str, ServiceConfig] = {}
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            self._services = {}
            return

        with self.path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        self._services = {}
        for name, config in data.items():
            if isinstance(config, dict):
                self._services[name] = ServiceConfig(
                    name=name,
                    type=config.get("type", "process"),
                    start=config.get("start", ""),
                    stop=config.get("stop", ""),
                    autostart=config.get("autostart", False),
                    metadata={k: v for k, v in config.items() if k not in ["type", "start", "stop", "autostart"]},
                )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = {name: config.to_dict() for name, config in self._services.items()}
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)

    def add(self, config: ServiceConfig) -> None:
        self._services[config.name] = config
        self.save()

    def remove(self, name: str) -> None:
        self._services.pop(name, None)
        self.save()

    def get(self, name: str) -> Optional[ServiceConfig]:
        return self._services.get(name)

    def all(self) -> Iterator[ServiceConfig]:
        return iter(self._services.values())

    def list_names(self) -> list[str]:
        return list(self._services.keys())
