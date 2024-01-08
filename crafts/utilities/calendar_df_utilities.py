from csv_calendar.csv_calendar import MonthlyCalendar
from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import query_for_daily_entry
from utilities.date_time_utilities import format_timedelta_as_hhmm_ampm
import pandas as pd

def export_user_data(user: str, user_id: str, year: int, month: int, table_name: str, id_name: str, export_data_to_csv: bool) -> pd.DataFrame:
    """
    Export database entries for a given user or provider to a CSV file.
    """
    # Initialize instances
    database = MySQLDatabase()
    calendar = MonthlyCalendar(year, month)
    calendar.generate_calendar()

    # Process each day and export CSV
    process_days(user, user_id, database, calendar, table_name, id_name)

    # Clean calendar DataFrame
    calendar.clean()

    # Export to CSV
    if export_data_to_csv:
        export_to_csv(calendar, user_id)

    return calendar.calendar_df

def process_days(user: str, user_id: str, database: MySQLDatabase, calendar: MonthlyCalendar, table_name: str, id_name: str) -> None:
    """
    Process each day in the calendar, query for daily entries, and update the calendar.
    """
    for date in calendar.date_range:
        process_single_day(user_id, date, database, calendar, table_name, id_name)

def process_single_day(user_id: str, date, database: MySQLDatabase, calendar: MonthlyCalendar, table_name: str, id_name: str) -> None:
    """
    Process a single day in the calendar.
    """
    week_of_month = calculate_week_of_month(date, calendar.first_day_of_the_month)
    day_of_week = date.strftime("%A")
    daily_entry = query_for_daily_entry(database, user_id, date.year, date.month, date.day, table_name, id_name)

    update_calendar_if_entry_exists(calendar, week_of_month, day_of_week, daily_entry)

def calculate_week_of_month(date, first_day_of_the_month) -> int:
    """
    Calculate the week of the month for a given date.
    """
    return (date.day + first_day_of_the_month - 1) // 7 + 1

def update_calendar_if_entry_exists(calendar: MonthlyCalendar, week_of_month: int, day_of_week: str, daily_entry) -> None:
    """
    Update calendar with daily entry if it exists.
    """
    if daily_entry:
        update_calendar_with_entry(calendar, week_of_month, day_of_week, daily_entry)

def update_calendar_with_entry(calendar: MonthlyCalendar, week_of_month: int, day_of_week: str, daily_entry) -> None:
    """
    Update the calendar with a daily entry.
    """
    in_time, out_time, total_time = daily_entry[0]
    formatted_in_time = format_timedelta_as_hhmm_ampm(in_time) if in_time else in_time
    formatted_out_time = format_timedelta_as_hhmm_ampm(out_time) if out_time else out_time
    calendar.update_calendar(week_of_month, day_of_week, formatted_in_time, formatted_out_time, total_time)

def export_to_csv(calendar: MonthlyCalendar, user_id: str) -> None:
    """
    Export the calendar to a CSV file.
    """
    export_file_name = f"./csv_export/{user_id}.csv"
    calendar.export_csv(export_file_name)
    print(f"Exported {export_file_name}")