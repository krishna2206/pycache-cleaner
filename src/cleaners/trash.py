from send2trash import send2trash

from cleaners.base import CleanerStrategy


class CleanerByTrashing(CleanerStrategy):
    def clean(self, path: str) -> None:
        print(f"Moving to trash: {path}")
        send2trash(path)
