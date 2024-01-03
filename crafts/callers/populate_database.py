from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import insert_to_daily_log_table, insert_to_provider_log
from readers.csv_reader import CSV_Reader
from utilities.process_file_utilities import get_csv_files, process_file, get_provider_log

CSV_FOLDER = "./csv"

# column names
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

COLUMN_NAMES_DAILY_LOG = ["Date Entry", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]

def populate_database(provider_id: str) -> None:
    """
    Populates the database with daily logs and provider logs from CSV files.

    Reads CSV files from a predefined folder, processes them to extract daily logs and provider-specific logs,
    then inserts these logs into the MySQL database. It is designed to be used with a specific database schema
    and expects CSV files to follow a predefined format.

    Args:
        provider_id (str): The registered provider ID to associate the logs with.

    Returns:
        None: This function does not return anything.
    """
    my_database = MySQLDatabase()
    my_csv_reader = CSV_Reader()

    csv_files = get_csv_files(CSV_FOLDER)

    for csv_file in csv_files:
        daily_log_df = process_file(csv_file, my_csv_reader, COLUMN_NAMES_CRAFTS)
        provider_log = get_provider_log(daily_log_df, provider_id)
        insert_to_daily_log_table(my_database, daily_log_df, COLUMN_NAMES_DAILY_LOG)
        insert_to_provider_log(my_database, provider_log)
        print("=" * 130, "\n")