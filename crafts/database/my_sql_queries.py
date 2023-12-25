from database.my_sql_database import MySQLDatabase
from typing import List, Any

def insert_data(database: MySQLDatabase, data: tuple) -> None:
    """
    Inserts data into the DailyLog table of the database.

    Args:
        database (MySQLDatabase): The database connection object.
        data (tuple): A tuple containing all necessary data to be inserted.

    Returns:
        None: Indicates the data was inserted, relies on the database.execute_query method.
    """
    insert_query = "INSERT INTO DailyLog (DateEntry, LoginTime, SignOutTime, TotalTime, Status, ChildrenID) VALUES (%s, %s, %s, %s, %s, %s)"
    database.execute_query(insert_query, data)

def read_data(database: MySQLDatabase) -> List[Any]:
    """
    Reads all data from the DailyLog table of the database.

    Args:
        database (MySQLDatabase): The database connection object.

    Returns:
        List[Any]: A list of tuples containing the rows of DailyLog table.
    """
    read_query = "SELECT * FROM DailyLog"
    return database.read_query(read_query)
