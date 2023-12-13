# import pandas as pd
from my_sql_database import MySQLDatabase

def insert_data(database, data):
    pass

def read_data(database):
    read_query = "SELECT * FROM DailyLog"
    return database.read_query(read_query)

if __name__ == "__main__":
    database = MySQLDatabase()

    print(read_data(database))