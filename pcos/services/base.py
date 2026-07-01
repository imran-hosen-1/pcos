from abc import ABC, abstractmethod

from pcos.models.service import ServiceConfig


class Service(ABC):
    def __init__(self, config: ServiceConfig):
        self.config = config

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def restart(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def health(self):
        pass