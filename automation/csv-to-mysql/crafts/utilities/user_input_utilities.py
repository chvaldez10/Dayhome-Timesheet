import sys


def print_usage(msg=None):
    """Exit the program and print usage message"""
    if msg:
        print(msg)

    sys.exit(0)
