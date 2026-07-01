import json

from services.postgres import PostgreSQLService
from services.redis import RedisService


SERVICE_MAP = {
    "postgres": PostgreSQLService,
    "redis": RedisService,
}


class Engine:
    def __init__(self, registry_file="core/registry.json"):
        with open(registry_file, "r") as f:
            self.registry = json.load(f)

    def load_services(self):
        services = {}

        for name, cfg in self.registry.items():
            cls = SERVICE_MAP.get(name)

            if cls:
                services[name] = cls(name, cfg)

        return services