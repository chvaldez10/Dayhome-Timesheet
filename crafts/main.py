# user defined classes
from exceptions.sys_arg_error import SysArgError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.daily_log_utilities import generate_provider_log

# python libraries
import pandas as pd
import sys

# test data
TEST_CSV = "./csv/2023-12-12.csv"

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

    # Read and process the CSV file
    daily_log = my_csv_reader.read_csv(TEST_CSV)
    daily_log_df = pd.DataFrame(daily_log, columns=COLUMN_NAMES_CRAFTS)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)

    # Generate and print the provider log
    provider_log = generate_provider_log(daily_log_df, provider_id)
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
