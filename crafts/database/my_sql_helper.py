from database.my_sql_queries import insert_data, read_data
from database.my_sql_database import MySQLDatabase
from readers.json_reader import load_json

# python packages
import pandas as pd
from typing import Tuple, List, Optional

# json data
USER_FILENAME = "./json/users.json"
CHILD_ID_MAP = load_json(USER_FILENAME)


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
        child_id = CHILD_ID_MAP.get(row['Child Name'], None)
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

def query_for_daily_entry(database: MySQLDatabase, user_id: str, year: int, month: int, day:int) -> Optional[Tuple]:
    query_string = "SELECT SignInTime, SignOutTime, TotalTime FROM DailyLog WHERE ChildrenID = %s AND YEAR(DateEntry) = %s AND MONTH(DateEntry) = %s AND DAY(DateEntry) = %s"
    params = (user_id, year, month, day)

    try:
        return read_data(database, query_string, params)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None