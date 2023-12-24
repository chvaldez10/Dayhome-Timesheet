# classes
from my_sql_database import MySQLDatabase
from csv_reader import CSV_Reader

# python packages
import datetime

# test data
TEST_CSV = "./csv/2023-12-12.csv"
IN_TIME = "08:00:00"
IN_TIME_OBJ= datetime.datetime.strptime(IN_TIME, "%H:%M:%S").time()

OUT_TIME = "15:00:00"
OUT_TIME_OBJ = datetime.datetime.strptime(OUT_TIME, "%H:%M:%S").time()

TEST_DATA = (datetime.date(2023, 12, 9), IN_TIME_OBJ, OUT_TIME_OBJ, 9.05, 'Attendance Recorded', 'sweetrice001')

def insert_data(database, data):
    insert_query = "INSERT INTO DailyLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ChildrenID) VALUES (%s, %s, %s, %s, %s, %s)"
    return database.execute_query(insert_query, data)

def read_data(database):
    read_query = "SELECT * FROM DailyLog"
    return database.read_query(read_query)

###########################################################
#
#            Main loop for input_processing.py
#
##########################################################

if __name__ == "__main__":
    # my database
    database = MySQLDatabase()

    # testing insert
    try:
        insert_data(database, TEST_DATA)
    except Exception as e:
        print(f"{e}")

    # my csv reader
    my_csv_reader = CSV_Reader()
    daily_log = my_csv_reader.read_csv(TEST_CSV)
    for log in daily_log:
        print(log)