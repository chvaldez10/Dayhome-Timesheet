from database.my_sql_queries import insert_data, read_data
from database.my_sql_database import MySQLDatabase
from readers.json_reader import load_json

# python packages
import pandas as pd
from typing import Tuple, List, Optional
import logging

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)


def insert_to_daily_log_table(database: MySQLDatabase, provider_log_df: pd.DataFrame, column_names: List[str]) -> None:
    """
    Inserts log entries from the dataframe to the DailyLog table in the database.

    Args:
        database (MySQLDatabase): The database connection object.
        provider_log_df (pd.DataFrame): The dataframe containing log data to insert.
        column_names (List[str]): List of column names to be inserted in order.

    Returns:
        None: Function does not return anything.
    """

    insert_query = "INSERT INTO DailyLog (DateEntry, Location, Status, SignInTime, SignOutTime, TotalTime, HealthCheck, ChildrenID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    for index, row in provider_log_df.iterrows():
        data_to_insert = [row[column_name] for column_name in column_names]
        child_id = USER_ID_MAP.get(row['Child Name'], None)
        data_to_insert.append(child_id)
        try:
            insert_data(database, insert_query, tuple(data_to_insert))
        except Exception as e:
            print(f"Error inserting data: {e}")

def insert_to_provider_log(database: MySQLDatabase, data_to_insert: Tuple) -> None:
    insert_query = "INSERT INTO ProviderLog (DateEntry, SignInTime, SignOutTime, TotalTime, ProviderID) VALUES (%s, %s, %s, %s, %s)"
    try:
        insert_data(database, insert_query, tuple(data_to_insert))
    except Exception as e:
        print(f"Error inserting data: {e}")

def query_for_daily_entry(database: MySQLDatabase, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str) -> Optional[Tuple]:
    """
    Query the database for entry records of a user or provider on a specific day.

    Args:
        database: An instance of MySQLDatabase.
        user_id: The unique identifier for the user or provider.
        year: The year of the record.
        month: The month of the record.
        day: The day of the record.
        table_name: The name of the table to query data from.
        id_name: The column name of the user or provider ID in the database.

    Returns:
        A tuple of SignInTime, SignOutTime, TotalTime if entry exists; None otherwise.
    """
    query_string = f"SELECT SignInTime, SignOutTime, TotalTime FROM {table_name} WHERE {id_name} = %s AND YEAR(DateEntry) = %s AND MONTH(DateEntry) = %s AND DAY(DateEntry) = %s"
    params = (user_id, year, month, day)

    try:
        return read_data(database, query_string, params)
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return None
    
def query_for_daily_total(database: MySQLDatabase, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str):
    """
    Query the database for the daily total of a user or provider on a specific day.

    Args:
        database: An instance of MySQLDatabase.
        user_id: The unique identifier for the user or provider.
        year: The year of the record.
        month: The month of the record.
        day: The day of the record.
        table_name: The name of the table to query data from.
        id_name: The column name of the user or provider ID in the database.

    Returns:
        A tuple of SignInTime, SignOutTime, TotalTime if entry exists; None otherwise.
    """
    query_string = f"SELECT TotalTime FROM {table_name} WHERE {id_name} = %s AND YEAR(DateEntry) = %s AND MONTH(DateEntry) = %s AND DAY(DateEntry) = %s"
    params = (user_id, year, month, day)

    try:
        return read_data(database, query_string, params)
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return None
    
def query_for_monthly_total(database: MySQLDatabase, user_id: str, year: int, month: int, table_name: str, id_name: str):
    """
    Query the database for the monthly total of a user or provider on a specific day.

    Args:
        database: An instance of MySQLDatabase.
        user_id: The unique identifier for the user or provider.
        year: The year of the record.
        month: The month of the record.
        table_name: The name of the table to query data from.
        id_name: The column name of the user or provider ID in the database.

    Returns:
        A tuple of SignInTime, SignOutTime, TotalTime if entry exists; None otherwise.
    """
    query_string = """SELECT SUM(TotalTime) FROM {table_name} WHERE {id_name} = %s AND YEAR(DateEntry) = %s AND MONTH(DateEntry) = %s GROUP BY Year(DateEntry), Month(DateEntry),  {id_name}""".format(table_name=table_name, id_name=id_name)

    params = (user_id, year, month)

    try:
        return read_data(database, query_string, params)
    except Exception as e:
        logging.error(f"Error executing query: {e}")
        return None