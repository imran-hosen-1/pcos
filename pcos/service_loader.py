import importlib
import inspect
import pkgutil

from pcos.services.base import Service
import pcos.services


def discover_services():
    services = {}

    for _, module_name, _ in pkgutil.iter_modules(pcos.services.__path__):

        if module_name == "base":
            continue

        module = importlib.import_module(
            f"pcos.services.{module_name}"
        )

        for _, obj in inspect.getmembers(module):

            if (
                inspect.isclass(obj)
                and issubclass(obj, Service)
                and obj is not Service
            ):
                services[module_name] = obj

    return services