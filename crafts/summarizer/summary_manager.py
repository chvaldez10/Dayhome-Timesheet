from database.my_sql_database import MySQLDatabase
from readers.json_reader import load_json
from database.my_sql_helper import query_for_monthly_total, query_for_daily_entry
from utilities.date_time_utilities import format_timedelta_as_hhmm_ampm

USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

class SummaryManager:
    """
    Manages and summarizes daily data entries for a given provider and children from a SQL database.

    Attributes:
        provider_id (str): Unique identifier for the provider.
        year (int): Year of the summary.
        month (int): Month of the summary.
        day (int): Day of the summary.
        database (MySQLDatabase): Instance of the database connection.

    Methods:
        summarize_day: Compiles a summary of daily entries for the provider and children.
        get_daily_summary: Retrieves and formats daily entry data for a single user.
    """
    def __init__(self, provider_id: str, year: int, month: int, day: int):
        """
        Initializes the SummaryManager with the specified provider ID, date, and database connection.

        Args:
            provider_id (str): Unique identifier for the provider.
            year (int): Year of the summary.
            month (int): Month of the summary.
            day (int): Day of the summary.
        """
        self.provider_id = provider_id
        self.year = year
        self.month = month
        self.day = day
        self.database = MySQLDatabase()

    def summarize_day(self) -> dict:
        """
        Retrieves and compiles a daily summary of logs for the provider and children.
        """
        user_data = {}

        print(f"\nDaily Summary for {self.year}/{self.month}/{self.day}\n" + "="*50)
        self._get_daily_summary("Me", self.provider_id, "ProviderLog", "ProviderID", user_data)
        for user, user_id in USER_ID_MAP.items():
            self._get_daily_summary(user, user_id, "DailyLog", "ChildrenID", user_data)

        return user_data

    def _get_daily_summary(self, user: str, user_id: str, table_name: str, id_name: str, user_data: dict):
        """
        Retrieves and formats the daily entry data for a single user from the database.
        """
        daily_entry = query_for_daily_entry(self.database, user_id, self.year, self.month, self.day, table_name, id_name)
        
        if daily_entry:
            in_time, out_time, total_time = daily_entry[0]
            in_time = format_timedelta_as_hhmm_ampm(in_time) if in_time else "N / A"
            out_time = format_timedelta_as_hhmm_ampm(out_time) if out_time else "N / A"
            user_data[user] = [in_time, out_time, total_time]

    def summarize_month(self) -> dict:
        user_data = {}
        self._get_monthly_summary("Me", self.provider_id, "ProviderLog", "ProviderID", user_data)
        for user, user_id in USER_ID_MAP.items():
            self._get_monthly_summary(user, user_id, "DailyLog", "ChildrenID", user_data)

        return user_data

    def _get_monthly_summary(self, user: str, user_id: str, table_name: str, id_name: str, user_data: dict):
        monthly_total = query_for_monthly_total(self.database, user_id, self.year, self.month, table_name, id_name)

        if monthly_total:
            monthly_total = monthly_total[0][0] if monthly_total[0][0] else 0
            user_data[user] = monthly_total