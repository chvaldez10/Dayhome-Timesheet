# user defined classes
from exceptions.date_parsing_error import DateParsingError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.date_utilities import parse_for_valid_date

# python libraries
import pandas as pd

# test data
TEST_CSV = "./csv/2023-12-12.csv"

# column names 
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]


###########################################################
#
#            Main loop for input_processing.py
#
##########################################################

if __name__ == "__main__":
    # my database
    my_database = MySQLDatabase()

    # my csv reader
    my_csv_reader = CSV_Reader()
    daily_log = my_csv_reader.read_csv(TEST_CSV)

    # convert to pandas df
    daily_log_df = pd.DataFrame(daily_log, columns=COLUMN_NAMES_CRAFTS)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(daily_log_df)
