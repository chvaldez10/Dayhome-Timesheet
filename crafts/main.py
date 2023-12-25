# user defined classes
from exceptions.date_parsing_error import DateParsingError
from database.my_sql_database import MySQLDatabase
from database.my_sql_queries import insert_data, read_data
from readers.csv_reader import CSV_Reader
from utilities.date_utilities import parse_for_valid_date

# python packages
import re
from datetime import datetime

# test data
TEST_CSV = "./csv/2023-12-12.csv"

###########################################################
#
#            Main loop for input_processing.py
#
##########################################################

if __name__ == "__main__":
    # my database
    database = MySQLDatabase()

    # my csv reader
    my_csv_reader = CSV_Reader()

    # check if csv is valid
    try:
        csv_date = parse_for_valid_date(TEST_CSV)
        print(csv_date)
    except DateParsingError as e:
        print(f"{e}")

    # daily_log = my_csv_reader.read_csv(TEST_CSV)
    # for log in daily_log:
    #     print(log)