import importlib
import pkgutil

from services.base import Service


def discover_services():
    services = {}

    package = importlib.import_module("services")

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):

        if module_name == "base":
            continue

        module = importlib.import_module(f"services.{module_name}")

        for obj in module.__dict__.values():

            if (
                isinstance(obj, type)
                and issubclass(obj, Service)
                and obj is not Service
            ):
                services[module_name] = obj

    return services