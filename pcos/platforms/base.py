from abc import ABC, abstractmethod


class Platform(ABC):

    @abstractmethod
    def run(self, command: str):
        pass