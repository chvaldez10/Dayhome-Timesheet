"""
    main:           Used to test functional components for personalized timesheet tool.

    ...

    options:
        -v:         print version (not yet implemented)
        --version:  print version (not yet implemented)

    Usage:          main.py [-v] <provider_id>

    Arguments:
        Provider Id:                   registered provider id in local database
"""

# user defined classes
from exceptions.sys_arg_error import SysArgError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from utilities.user_input_utilities import print_usage 
from readers.csv_reader import CSV_Reader
from utilities.process_file_utilities import process_file, get_csv_files

# python libraries
import sys

# test data
CSV_FOLDER = "./csv"


###########################################################
#
#                        Main loop
#
##########################################################


def main(provider_id: str):
    # Setup database and CSV reader
    # my_database = MySQLDatabase()
    my_csv_reader = CSV_Reader()

    csv_files = get_csv_files(CSV_FOLDER)

    for csv_file in csv_files:
        process_file(csv_file, my_csv_reader, provider_id)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            provider_id = sys.argv[1]
            main(provider_id)
        else:
            raise SysArgError("No input provided.")
    except SysArgError as e:
        print(f"Error: {e}")
        print_usage(__doc__)
