from pcos.registry import Registry
from pcos.service_loader import discover_services


class Engine:

    def __init__(self):
        self.registry = Registry().load()
        self.available = discover_services()

    def list_services(self):
        return sorted(self.available.keys())