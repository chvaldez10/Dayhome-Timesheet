import pandas as pd
import re
from datetime import datetime

TEST_CSV = "2023-12-12.csv"

class CSV_Reader:
    def __init__(self) -> None:
        pass

    def read_csv(self, csv_file:str) -> list[tuple]:
        # read csv as dataframe
        df = pd.read_csv(csv_file)

        # drop unwanted columns
        df.drop(columns=["Unnamed: 0", "Provider", "Unnamed: 7", "Unnamed: 8"], inplace=True)
        
        # parse dataframe per row
        for index, row in df.iterrows():
            child_name = row["Child Name"]
            location = self.clean_location_string(row["Location/Room"])
            status = row["Status"]
            in_time, out_time, total_time = self.parse_datetime(row["Times"])
            health_check = row["Health Check"]

            print(in_time, type(in_time))
            print(child_name, location, status, in_time, out_time, total_time, health_check)
            break

    def clean_location_string(self, location:str) -> str:
        cleaned_location_string = location.split()
        cleaned_location_string = [word for word in cleaned_location_string if word != "---AGENCY"]
        return " ".join(cleaned_location_string)
    
    def parse_datetime(self, times: str):
        found_dates = re.findall(r"(\d{2}:\d{2} [AP]M)", times)
        
        if found_dates and len(found_dates) == 2:
            in_time = datetime.strptime(found_dates[0], '%I:%M %p').time()
            out_time = datetime.strptime(found_dates[1], '%I:%M %p').time()
            total_time = (datetime.combine(datetime.min, out_time) - datetime.combine(datetime.min, in_time)).seconds / 3600.0
            return in_time, out_time, total_time
        else:
            return None, None, None

my_csv_reader = CSV_Reader()
my_csv_reader.read_csv(TEST_CSV)