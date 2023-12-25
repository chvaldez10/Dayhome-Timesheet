import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

class MySQLDatabase:
    """
    A Data Access Object (DAO) class for managing interactions with a MySQL database.

    This class abstracts and encapsulates all access to the data source, providing
    methods to execute and read SQL queries. 

    Methods:
        __init__: Initializes the database connection.
        execute_query: Executes a given SQL query, given data.
        read_query: Executes a read operation and returns fetched results.
    """

    def __init__(self) -> None:
        # initialize connection
        self.connection = None

        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("DATABASE_HOST"),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                database=os.getenv("DATABASE_NAME")
            )
        except Error as e:
            print(f"Error connection to MySQL database: {e}")

    def execute_query(self, query, data=None) -> bool:
        """
        Executes SQL query.

        Args:
            query: MySQL command
            data: data to inser

        Returns:
            True for successful query. Otherwise, return false.
        """

        cursor = self.connection.cursor()

        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error executing data: {e}")
            return False

    def read_query(self, query) -> list:
        """
        Queries data from database.

        Args:
            query: MySQL query statement

        Returns:
            A list of tuples containing all results.
        """

        cursor = self.connection.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error reading data: {e}")
            return None