# Pycache cleaner

This is a simple script to clean the pycache folders from the current directory and all subdirectories.

## How to install

### From source

- Clone the repository

```bash
    git clone https://github.com/krishna2206/pycache-cleaner.git
```

- Install the requirements

```bash
    pip install -r requirements.txt
```

### From releases

- Download the latest binary executable from the releases page

## Usage

### From the python file (you must have python installed, and the requirements installed)

```bash
    python pycache_cleaner.py
```

### From the binary (windows)

```cmd
    pycache_cleaner.exe
```

### From the binary (linux)

```bash
    ./pycache_cleaner
```

## Options

```bash
    safe, --safe
        Move the pycache folders to the trash instead of deleting them.
    simulation, --simulation
        Do not delete or move the pycache folders, just print the paths.
```

### Warning

This script will delete all folders with the name `__pycache__` in the current directory and all subdirectories. If you have any folders with this name that you do not want to delete, you should move them before running the script.

## TODO

- Create binary executable for Windows

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
