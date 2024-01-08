import pandas as pd

# Constants for days of the week and the types of entries
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ENTRY_INDICES = ["In", "Out", "Total"]

class MonthlyCalendar:
    """A class to represent a monthly calendar that can be populated with time entries."""
    
    def __init__(self, year: int, month: int) -> None:
        """Initialize the MonthlyCalendar with a specific year and month."""
        self.year = year
        self.month = month
        self.date_range = self.get_date_range()
        self.first_day_of_the_month = self.date_range[0].dayofweek
        self.calendar_df = None

    def get_date_range(self) -> pd.DatetimeIndex:
        """Generate the date range for the month."""
        start_date = f"{self.year}-{self.month:02d}-01"
        end_date = pd.to_datetime(start_date) + pd.offsets.MonthEnd(0)
        return pd.date_range(start=start_date, end=end_date)

    def generate_calendar(self) -> None:
        """Generate a blank calendar with a multi-index for weeks and entry types."""
        num_days = len(self.date_range)
        num_weeks = (self.first_day_of_the_month + num_days - 1) // 7 + 1
        week_indices = range(1, num_weeks + 1)

        multi_index = pd.MultiIndex.from_product([week_indices, ENTRY_INDICES], names=["Week", "Entry"])
        self.calendar_df = pd.DataFrame(columns=DAYS_OF_WEEK, index=multi_index)

    def update_calendar(self, week_of_month: int, day_of_week: int, in_time: int, out_time:int, total_time: int) -> None:
        """Update the calendar with values from the database."""
        self.calendar_df.loc[(week_of_month, "In"), day_of_week] = in_time
        self.calendar_df.loc[(week_of_month, "Out"), day_of_week] = out_time
        self.calendar_df.loc[(week_of_month, "Total"), day_of_week] = total_time

    def print_calendar(self) -> None:
        """Print the calendar. If the calendar is not yet generated, indicate it's missing."""
        if self.calendar_df is not None:
            print(self.calendar_df)
        else:
            print("No calendar data found")

    def clean(self):
        """Add necessary commands to clean dataframe"""
        self.calendar_df.drop(["Saturday", "Sunday"], axis=1, inplace=True)
        self.calendar_df.fillna("", inplace=True)

    def export_csv(self, filename: str) -> None:
        """Export the calendar data to a CSV file. If the calendar is missing, notify the user."""
        if self.calendar_df is not None:
            self.calendar_df.to_csv(filename)
        else:
            print("No calendar data found")