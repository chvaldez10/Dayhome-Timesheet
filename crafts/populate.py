# user defined classes
from my_sql_database import MySQLDatabase
from csv_reader import CSV_Reader

# python packages
import re
from datetime import datetime

# regex patterns
DATE_PATTERN = r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"

# test data
TEST_CSV = "./csv/2023-12-12.csv"

# database actions
def insert_data(database, data) -> datetime.date:
    insert_query = "INSERT INTO DailyLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ChildrenID) VALUES (%s, %s, %s, %s, %s, %s)"
    return database.execute_query(insert_query, data)

def read_data(database):
    read_query = "SELECT * FROM DailyLog"
    return database.read_query(read_query)

# None class
class DateParsingError(Exception):
    """Exception raised when date parsing fails"""

# util functions
def parse_for_valid_date(date_string: str):
    """
    Parse the provided string for a valid date.

    Args:
        date_string (str): The string containing the date.

    Returns:
        datetime.date: The extracted date object.

    Raises:
        DateParsingError: If no valid date is found.
    """
    date_match = re.search(DATE_PATTERN, date_string)
    if date_match:
        date_str = date_match.group(0)

        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise DateParsingError(f"Invalid date format: {date_str}")
    raise DateParsingError("No matched date.")

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
    except Exception as e:
        print(f"{e}")

    # daily_log = my_csv_reader.read_csv(TEST_CSV)
    # for log in daily_log:
    #     print(log)