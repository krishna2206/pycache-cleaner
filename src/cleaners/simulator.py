from cleaners.base import CleanerStrategy


class CleanerSimulator(CleanerStrategy):
    def clean(self, path: str) -> None:
        print(f"To be removed: {path}")
