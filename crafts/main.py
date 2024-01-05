"""
    main:           Used to test functional components for personalized time sheet tool.

    ...

    options:
        -v, --version:         print version (not yet implemented)
        -p, --populate:        populate database
        -q, --query:           query database (takes an additional argument)
        -e, --export:          export to CSV file (takes an additional argument)

    Usage:          main.py <provider_id> [-v] [-p] [-q QUERY] [-e EXPORT]

    Arguments:
        Provider Id:                   registered provider id in local database
"""

# user defined classes
from utilities.user_input_utilities import print_usage
from callers.populate_database import populate_database
from callers.export_database import export_database

# python libraries
import argparse

###########################################################
#
#                        Main loop
#
##########################################################

def main() -> None:
    parser = argparse.ArgumentParser(description="Process daily log files for a provider.")
    parser.add_argument("provider_id", metavar="provider_id", type=str, help="registered provider id in local database")
    parser.add_argument("-v", "--version", action="store_true", help="print version number and exit")
    parser.add_argument("-p", "--populate", action="store_true", help="populate database with data from CSV files")
    parser.add_argument("-s", "--summary", nargs="+", help="query daily summary")
    parser.add_argument("-e", "--export", nargs="+", help="export to CSV file by month")

    args = parser.parse_args()

    # initialize classes

    if args.version:
        print("Version 24.0.0")

    if args.populate:
        populate_database(args.provider_id)

    if args.export:
        year = int(args.export[0])
        month = int(args.export[1])

        export_database(args.provider_id, year, month)

    if args.summary:
        year = int(args.summary[0])
        month = int(args.summary[1])

if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print_usage(__doc__)
        print(f"Error: {e}")