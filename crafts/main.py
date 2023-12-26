# user defined classes
from exceptions.sys_arg_error import SysArgError
from exceptions.date_parsing_error import DateParsingError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.date_utilities import parse_for_valid_date
from utilities.daily_log_utilities import generate_provider_log

# python libraries
import os
import pandas as pd
import sys
from datetime import datetime

# test data
CSV_FOLDER = "./csv"

# column names 
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

# config to see all columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


###########################################################
#
#                        Main loop
#
##########################################################


def main(provider_id: str):
    # Setup database and CSV reader
    # my_database = MySQLDatabase()
    my_csv_reader = CSV_Reader()

    csv_files = sorted(os.listdir(CSV_FOLDER))

    for csv_file in csv_files:
        temp_filename = os.path.join(CSV_FOLDER, csv_file)
        print(csv_file)
        try:
            parse_for_valid_date(csv_file)
        except DateParsingError as e:
            print(f"{e}\nInvalid filename: {temp_filename}")
        else:
            # Read and process the CSV file
            daily_log = my_csv_reader.read_csv(temp_filename)
            daily_log_df = pd.DataFrame(daily_log, columns=COLUMN_NAMES_CRAFTS)
            provider_log = generate_provider_log(daily_log_df, provider_id)
            print(daily_log_df)
            print(provider_log)


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
