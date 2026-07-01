import json

from service_loader import discover_services


class Engine:

    def __init__(self, registry_file="core/registry.json"):

        with open(registry_file) as f:
            self.registry = json.load(f)

        self.available = discover_services()

    def load_services(self):

        loaded = {}

        for name, cfg in self.registry.items():

            cls = self.available.get(name)

            if cls:

                loaded[name] = cls(name, cfg)

        return loaded