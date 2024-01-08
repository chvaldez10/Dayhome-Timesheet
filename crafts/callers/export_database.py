from csv_calendar.csv_calendar import MonthlyCalendar
from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import query_for_daily_entry
from utilities.date_time_utilities import format_timedelta_as_hhmm_ampm
from utilities.calendar_df_utilities import export_user_data
from readers.json_reader import load_json

# json data
USER_FILENAME = "./json/users.json"
user_id_map = load_json(USER_FILENAME)

def export_database(provider_id: str, year: int, month: int) -> None:
    """
    Export database records for users and a provider to CSV files.
    """
    for user, user_id in user_id_map.items():
        calendar_df = export_user_data(user, user_id, year, month, "DailyLog", "ChildrenID", True)

    calendar_df = export_user_data("Provider", provider_id, year, month, "ProviderLog", "ProviderID", True)