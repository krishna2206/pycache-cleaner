import os
import sys

from cleaners.delete import CleanerByRemoving
from cleaners.simulator import CleanerSimulator
from cleaners.trash import CleanerByTrashing


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--safe':
            cleaner = CleanerByTrashing()
        elif sys.argv[1] == '--simulation':
            cleaner = CleanerSimulator()
        else:
            print("Usage:")
            print("pycachecleaner [--safe] [--simulation]\n")
            print("Options:")
            print("--safe: Move __pycache__ folders to trash")
            print("--simulation: Show what would be removed\n")
            print("If no option is given, the script will remove the __pycache__ folders")
            print("The two options can't be used together, the first option will be used if both are given")
            exit(1)
    else:
        cleaner = CleanerByRemoving()
    

    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            if dir == "__pycache__":
                path = os.path.join(root, dir)
                cleaner.clean(path)

if __name__ == "__main__":
    main()
