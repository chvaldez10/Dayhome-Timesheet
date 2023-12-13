# import pandas as pd
from my_sql_database import MySQLDatabase
import datetime

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
    test_data = (datetime.date(2023, 12, 9), datetime.timedelta(seconds=29581), datetime.timedelta(seconds=62101), 9.05, 'Attendance Recorded', 'sweetrice001')

    database = MySQLDatabase()
    insert_data(database, test_data)

    print(read_data(database))