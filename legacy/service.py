from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterator, Optional


@dataclass
class Service:
    name: str
    enabled: bool = True
    metadata: Dict[str, object] = None

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "enabled": self.enabled,
            "metadata": self.metadata or {},
        }


class ServiceRegistry:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._services: Dict[str, Service] = {}
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            self._services = {}
            return

        with self.path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        self._services = {
            item["name"]: Service(
                name=item["name"],
                enabled=item.get("enabled", True),
                metadata=item.get("metadata", {}),
            )
            for item in data
            if "name" in item
        }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump([service.to_dict() for service in self._services.values()], handle, indent=2)

    def add(self, service: Service) -> None:
        self._services[service.name] = service
        self.save()

    def remove(self, name: str) -> None:
        self._services.pop(name, None)
        self.save()

    def get(self, name: str) -> Optional[Service]:
        return self._services.get(name)

    def all(self) -> Iterator[Service]:
        return iter(self._services.values())


class ServiceManager:
    def __init__(self, registry: ServiceRegistry) -> None:
        self.registry = registry

    def start_service(self, name: str) -> bool:
        service = self.registry.get(name)
        if service is None or not service.enabled:
            return False
        return True

    def stop_service(self, name: str) -> bool:
        service = self.registry.get(name)
        return bool(service)

    def list_services(self) -> Iterator[Service]:
        return self.registry.all()
