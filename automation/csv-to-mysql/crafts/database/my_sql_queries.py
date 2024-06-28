from database.my_sql_database import MySQLDatabase
from typing import List, Any

def insert_data(database: MySQLDatabase, query: str, data: tuple) -> None:
    """
    Inserts data into a table of the database using the provided query.

    Args:
        database (MySQLDatabase): The database connection object.
        query (str): SQL query string.
        data (tuple): A tuple containing all necessary data to be inserted.

    Returns:
        None: Indicates the function does not return anything.
    """
    try:
        database.execute_query(query, data)
    except Exception as e:
        print(f"Error executing query: {e}")

def read_data(database: MySQLDatabase, query: str, data: tuple) -> List[Any]:
    """
    Reads all data from the DailyLog table of the database.

    Args:
        database (MySQLDatabase): The database connection object.

    Returns:
        List[Any]: A list of tuples containing the rows of DailyLog table.
    """
    try:
        return database.read_query(query, data)
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
