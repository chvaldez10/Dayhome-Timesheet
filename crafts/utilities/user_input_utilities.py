import sys


def print_usage(msg=None):
    """Exit the program and print usage message"""
    print(__doc__)

    if msg:
        print(msg)

    sys.exit(0)
