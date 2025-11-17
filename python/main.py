import os
import subprocess
import sys


def main():
    for filename in os.listdir("."):
        if filename.startswith("day") and filename.endswith(".py"):
            print(f"====== Running {filename} ======")
            subprocess.run([sys.executable, filename])


if __name__ == "__main__":
    main()
