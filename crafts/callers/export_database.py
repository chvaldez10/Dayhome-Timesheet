from csv_calendar.csv_calendar import MonthlyCalendar
from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import query_for_daily_entry
from utilities.date_time_utilities import format_timedelta_as_hhmm_ampm
from readers.json_reader import load_json

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def export_database(provider_id:str, year: int, month: int) -> None:
    """
    Export database records for all users and a provider to CSV files.

    Args:
        provider_id: The unique identifier for the provider.
        year: The year of the records to be exported.
        month: The month of the records to be exported.
    """

    for user, user_id in USER_ID_MAP.items():
        export_user_data(user, user_id, year, month, "DailyLog", "ChildrenID")
    
    export_user_data("Provider", provider_id, year, month, "ProviderLog", "ProviderID")

def export_user_data(user: str, user_id: str, year: int, month: int, table_name: str, id_name: str) -> None:
    """
    Helper function to export database entries for a given user or provider to a CSV file.

    Args:
        user: The user's name or "Provider" for providers.
        user_id: The unique identifier for the user or provider.
        year: The year of the records to be exported.
        month: The month of the records to be exported.
        table_name: The name of the table to query data from.
        id_name: The column name of the user or provider ID in the database.
    """
    # Initialize database and calendar instances
    my_database = MySQLDatabase()
    my_calendar = MonthlyCalendar(year, month)
    my_calendar.generate_calendar()

    # Process each day and export CSV
    process_days_and_export(user, user_id, my_database, my_calendar, table_name, id_name)

def process_days_and_export(user: str, user_id: str, database: MySQLDatabase, calendar: MonthlyCalendar, table_name: str, id_name: str) -> None:
    """
    Process each day in the calendar, query for daily entries, and export the calendar to CSV.

    Args:
        user: The user's name or "Provider" for providers.
        user_id: The unique identifier for the user or provider.
        database: An instance of MySQLDatabase.
        calendar: An instance of MonthlyCalendar.
        table_name: The name of the table to query data from.
        id_name: The column name of the user or provider ID in the database.
    """
    for date in calendar.date_range:
        week_of_month = (date.day + calendar.first_day_of_the_month - 1) // 7 + 1
        day_of_week = date.strftime("%A")
        daily_entry = query_for_daily_entry(database, user_id, date.year, date.month, date.day, table_name, id_name)

        # Update calendar or log warning for missing entry
        if daily_entry:
            in_time, out_time, total_time = daily_entry[0]
            in_time = format_timedelta_as_hhmm_ampm(in_time) if in_time else in_time
            out_time = format_timedelta_as_hhmm_ampm(out_time) if out_time else out_time
            calendar.update_calendar(week_of_month, day_of_week, in_time, out_time, total_time)
        
    # Export calendar to CSV
    export_file_name = f"./csv_export/{user_id}.csv"
    calendar.export_csv(export_file_name)
    print(f"Exported {export_file_name}")