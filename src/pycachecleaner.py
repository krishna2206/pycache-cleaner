import os
import sys
import shutil

import send2trash


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--safe':
            safe_mode()
        elif sys.argv[1] == '--simulation':
            simulation_mode()
        else:
            print("Usage:")
            print("pycachecleaner [--safe] [--simulation]\n")
            print("Options:")
            print("--safe: Move __pycache__ folders to trash")
            print("--simulation: Show what would be removed\n")
            print("If no option is given, the script will remove the __pycache__ folders")
            print("The two options can't be used together, the first option will be used if both are given")
    else:
        normal_mode()


def normal_mode():
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            if dir == "__pycache__":
                print("Removing: " + os.path.join(root, dir))
                shutil.rmtree(os.path.join(root, dir))


def safe_mode():
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            if dir == "__pycache__":
                print("Moving to trash: " + os.path.join(root, dir))
                send2trash.send2trash(os.path.join(root, dir))


def simulation_mode():
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            if dir == "__pycache__":
                print("To be removed: " + os.path.join(root, dir))


if __name__ == "__main__":
    main()
