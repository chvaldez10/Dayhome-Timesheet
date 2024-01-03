"""
    main:           Used to test functional components for personalized time sheet tool.

    ...

    options:
        -v, --version:         print version (not yet implemented)
        -p, --populate:        populate database
        -q, --query:           query database (takes an additional argument)
        -e, --export:          export to CSV file (takes an additional argument)

    Usage:          main.py [-v] [-p] [-q QUERY] [-e EXPORT] <provider_id>

    Arguments:
        Provider Id:                   registered provider id in local database
"""

# user defined classes
from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import insert_to_daily_log_table, insert_to_provider_log
from utilities.user_input_utilities import print_usage
from readers.csv_reader import CSV_Reader
from utilities.process_file_utilities import process_file, get_csv_files, get_provider_log

# python libraries
import argparse

# data
CSV_FOLDER = "./csv"

# column names
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

COLUMN_NAMES_DAILY_LOG = ["Date Entry", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

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
    parser.add_argument("-q", "--query", help="query database by month")
    parser.add_argument("-e", "--export", help="export to CSV file by month")

    args = parser.parse_args()

    # Setup database and CSV reader
    my_database = MySQLDatabase()
    my_csv_reader = CSV_Reader()
    csv_files = get_csv_files(CSV_FOLDER)

    if args.version:
        print("Version 24.0.0")
        return

    if args.populate:
        for csv_file in csv_files:
            daily_log_df = process_file(csv_file, my_csv_reader, COLUMN_NAMES_CRAFTS)
            provider_log = get_provider_log(daily_log_df, args.provider_id)
            insert_to_daily_log_table(my_database, daily_log_df, COLUMN_NAMES_DAILY_LOG)
            insert_to_provider_log(my_database, provider_log)
            print("=" * 130, "\n")

    if args.export:
        print(args.export)

    if args.query:
        print(args.query)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print_usage(__doc__)
        print(f"Error: {e}")