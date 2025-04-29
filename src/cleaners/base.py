from abc import ABC, abstractmethod


class CleanerStrategy(ABC):
    @abstractmethod
    def clean(self, path: str) -> None: ...