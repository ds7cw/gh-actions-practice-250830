import platform
import sys


def main() -> None:
    """Prints the Python version and operating system of the host"""
    print("Running on Python {}".format(sys.version))
    print("Operating System: {} {}".format(platform.system(), platform.release()))


if __name__ == "__main__":
    main()
