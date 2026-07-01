import json
from pathlib import Path

from pcos.models.service import ServiceConfig


class Registry:
    def __init__(self, path="configs/registry.json"):
        self.path = Path(path)

    def load(self):
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        configs = {}

        for name, cfg in data.items():
            configs[name] = ServiceConfig(
                name=name,
                enabled=cfg.get("enabled", True),
                autostart=cfg.get("autostart", False),
                depends_on=cfg.get("depends_on", []),
            )

        return configs