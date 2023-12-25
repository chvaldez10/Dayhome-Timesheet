# user defined classes
from exceptions.date_parsing_error import DateParsingError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.date_utilities import parse_for_valid_date
from utilities.daily_log_utilities import generate_provider_log

# python libraries
import pandas as pd
from datetime import datetime

# test data
TEST_CSV = "./csv/2023-12-12.csv"

# column names 
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]


###########################################################
#
#                        Main loop
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
    # daily_log_df["In Time"] = pd.to_datetime(daily_log_df["In Time"], format="%H:%M:%S", errors="coerce").dt.time
    # daily_log_df["Out Time"] = pd.to_datetime(daily_log_df["Out Time"], format="%H:%M:%S", errors="coerce").dt.time
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # print(daily_log_df.dtypes)
    # print(daily_log_df)

    generate_provider_log(daily_log_df)