# user defined classes
from exceptions.sys_arg_error import SysArgError
from exceptions.date_parsing_error import DateParsingError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.date_utilities import parse_for_valid_date
from utilities.daily_log_utilities import generate_provider_log
from utilities.process_file_utilities import process_file, get_csv_files

# python libraries
import os
import pandas as pd
import sys
from datetime import datetime

# test data
CSV_FOLDER = "./csv"

# column names 
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

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
        print("Usage: script.py <provider_id>")
