from utilities.date_utilities import parse_for_valid_date
from exceptions.date_parsing_error import DateParsingError
from readers.csv_reader import CSV_Reader
from utilities.daily_log_utilities import generate_provider_log

# python packages
import pandas as pd
from typing import List, Tuple, Optional, Any
import os

# config to see all columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# column names 
COLUMN_NAMES_CRAFTS = ["Date Entry", "Child Name", "Location", "Status", "In Time", "Out Time", "Total Time", "Health Record"]


def process_file(filename: str, reader: CSV_Reader) -> Optional[pd.DataFrame]:
    """
    Process each CSV file: read, convert to DataFrame, and generate logs.
    :param filename: The name of the file to process.
    :param reader: CSV Reader instance with a method read_csv.
    :return: A pandas DataFrame of the processed file or None if an error occurs.
    """
    try:
        parse_for_valid_date(filename)  # Validate date or filename
        daily_log = reader.read_csv(filename)
        daily_log_df = pd.DataFrame(daily_log, columns=COLUMN_NAMES_CRAFTS)
        print(daily_log_df)
        return daily_log_df
    except DateParsingError as e:
        print(f"{e}\nInvalid filename: {filename}")
        return None


def get_provider_log(daily_log_df: pd.DataFrame, provider_id: str) -> Tuple[Any, ...]:
    """
    Extracts logs for a specific provider from the daily log DataFrame.
    :param daily_log_df: DataFrame containing daily logs.
    :param provider_id: The provider's identifier to filter logs.
    :return: A tuple containing the provider's log.
    """
    provider_log = generate_provider_log(daily_log_df, provider_id)
    print(provider_log)
    return provider_log

def get_csv_files(folder_path: str) -> List[str]:
    """Get sorted list of CSV files from the given folder."""
    return sorted(os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".csv"))