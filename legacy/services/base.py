from abc import ABC, abstractmethod


class Service(ABC):
    def __init__(self, name, config):
        self.name = name
        self.config = config

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass
    