import pandas as pd
import numpy as np

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ENTRY_INDICES = ["In", "Out", "Total"]

class MonthlyCalendar:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month
        self.date_range = self.get_date_range()
        self.first_day_of_the_month = self.date_range[0].dayofweek
        self.calendar_df = None

    def get_date_range(self) -> pd.DatetimeIndex:
        start_date = f"{self.year}-{self.month:02d}-01"
        end_date = pd.to_datetime(start_date) + pd.offsets.MonthEnd(0)
        return pd.date_range(start=start_date, end=end_date)

    def generate_calendar(self) -> pd.DataFrame:
        num_days = len(self.date_range)
        num_weeks = (self.first_day_of_the_month + num_days - 1) // 7 + 1
        week_indices = range(1, num_weeks)

        multi_index = pd.MultiIndex.from_product([week_indices, ENTRY_INDICES], names=["Week", "Entry"])

        self.calendar_df = pd.DataFrame(
            columns=DAYS_OF_WEEK,
            index=multi_index
        )

    def populate_calendar(self) -> None:
        for date in self.date_range:
            week_of_month = (date.day + self.first_day_of_the_month - 1) // 7 + 1
            day_of_week = date.strftime('%A')
            self.calendar_df.loc[(week_of_month, "In"), day_of_week] = "8:00 AM"
            self.calendar_df.loc[(week_of_month, "Out"), day_of_week] = "5:00 PM"
            self.calendar_df.loc[(week_of_month, "Total"), day_of_week] = "8"
            # self.calendar_df.at[week_of_month, day_of_week] = date.strftime("%m/%d")
        
        self.calendar_df.fillna("")

    def print_calendar(self) -> None:
        if self.calendar_df is not None:
            print(self.calendar_df)
        else:
            print("No calendar data found")

    def export_csv(self, filename:str) -> None:
        if self.calendar_df is not None:
            self.calendar_df.to_csv(filename)
        else:
            print("No calendar data found")

my_calendar = MonthlyCalendar(2024, 1)
my_calendar.generate_calendar()
my_calendar.print_calendar()
my_calendar.populate_calendar()
my_calendar.print_calendar()
my_calendar.export_csv("calendar.csv")