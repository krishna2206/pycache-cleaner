import shutil

from cleaners.base import CleanerStrategy


class CleanerByRemoving(CleanerStrategy):
    def clean(self, path: str) -> None:
        print(f"Removing: {path}")
        shutil.rmtree(path)