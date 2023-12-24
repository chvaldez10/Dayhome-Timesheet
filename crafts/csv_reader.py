import pandas as pd
import re
from datetime import datetime
import math

TEST_CSV = "./csv/2023-12-12.csv"

class CSV_Reader:
    def __init__(self) -> None:
        """Initialize the CSV Reader class."""
        pass

    def read_csv(self, csv_file: str) -> list[tuple]:
        """
        Reads a CSV file and processes its content.
        Args:
            csv_file (str): The path to the CSV file.
        Returns:
            list[tuple]: A list of tuples containing processed data from the CSV.
        """
        try:
            df = pd.read_csv(csv_file)
            df.drop(columns=["Unnamed: 0", "Provider", "Unnamed: 7", "Unnamed: 8"], inplace=True)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []

        daily_log = []
        for _, row in df.iterrows():
            child_name = row["Child Name"]
            location = self.clean_location_string(row["Location/Room"])
            status = row["Status"]
            in_time, out_time, total_time = self.parse_datetime(str(row["Times"]))
            health_check = str(row["Health Check"]) if pd.notna(row["Health Check"]) else None

            daily_log.append((child_name, location, status, in_time, out_time, total_time, health_check))

        return daily_log

    def clean_location_string(self, location: str) -> str:
        """
        Cleans a location string by removing specific unwanted parts.
        Args:
            location (str): The location string to clean.
        Returns:
            str: The cleaned location string.
        """
        cleaned_location_string = [word for word in location.split() if word != "---AGENCY"]
        return " ".join(cleaned_location_string)
    
    def parse_datetime(self, times: str) -> tuple:
        """
        Parses a datetime string and calculates the total time.
        Args:
            times (str): The datetime string to parse.
        Returns:
            tuple: A tuple containing in_time, out_time, and total_time.
        """
        if not times:
            return None, None, 0
        
        found_dates = re.findall(r"(\d{2}:\d{2} [AP]M)", times)
        if len(found_dates) != 2:
            return None, None, 0

        in_time = datetime.strptime(found_dates[0], '%I:%M %p').time()
        out_time = datetime.strptime(found_dates[1], '%I:%M %p').time()
        total_time = (datetime.combine(datetime.min, out_time) - datetime.combine(datetime.min, in_time)).seconds / 3600.0
        
        return in_time, out_time, total_time