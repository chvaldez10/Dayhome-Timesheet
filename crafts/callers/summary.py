from database.my_sql_database import MySQLDatabase
from emailer.email_sender import EmailSender
from readers.json_reader import load_json
from utilities.date_time_utilities import format_timedelta_as_hhmm_ampm, format_year_month_day
from database.my_sql_helper import query_for_monthly_total, query_for_daily_entry

import os

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

class SummaryManager:
    def __init__(self, provider_id: str, year: int, month: int, day: int):
        self.provider_id = provider_id
        self.year = year
        self.month = month
        self.day = day
        self.database = MySQLDatabase()

    def summarize_day(self) -> dict:
        pass

    def get_daily_summary(self, user: str, user_id: str, table_name: str, id_name: str, user_data: dict):
        pass

    def summarize_month(self):
        pass

    def get_monthly_summary(self, user: str, user_id: str, table_name: str, id_name: str):
        pass

def summarizer(provider_id:str, year: int, month: int, day:int) -> None:
    formatted_year_month_day = format_year_month_day(year, month, day)
    my_email_sender = EmailSender(formatted_year_month_day)
    user_data = summarize_day(provider_id, year, month, day)
    my_email_sender.user_data = user_data
    my_email_sender.send_email(f"Summary for {formatted_year_month_day} 🏠")
    # summarize_month(provider_id, year, month, day)

def summarize_day(provider_id: str, year: int, month: int, day: int) -> dict:
    user_data = {}

    print(f"\nDaily Summary for {year}/{month}/{day}\n" + "="*50)
    get_daily_summary("Me", provider_id, year, month, day, "ProviderLog", "ProviderID", user_data)
    for user, user_id in USER_ID_MAP.items():
        get_daily_summary(user, user_id, year, month, day, "DailyLog", "ChildrenID", user_data)

    return user_data

def get_daily_summary(user: str, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str, user_data: dict) -> None:
    my_database = MySQLDatabase()
    daily_entry = query_for_daily_entry(my_database, user_id, year, month, day, table_name, id_name)
    
    if daily_entry:
        in_time, out_time, total_time = daily_entry[0]
        in_time = format_timedelta_as_hhmm_ampm(in_time) if in_time else "N / A"
        out_time = format_timedelta_as_hhmm_ampm(out_time) if out_time else "N / A"
        user_data[user] = [in_time, out_time, total_time]

def summarize_month(provider_id: str, year: int, month: int, day:int) -> None:
    print(f"\nMonthly Summary for {year}/{month}/{day}\n" + "="*50)
    get_monthly_summary("Me", provider_id, year, month, day, "ProviderLog", "ProviderID")
    for user, user_id in USER_ID_MAP.items():
        get_monthly_summary(user, user_id, year, month, day, "DailyLog", "ChildrenID")

def get_monthly_summary(user: str, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str) -> None:
    my_database = MySQLDatabase()
    monthly_total = query_for_monthly_total(my_database, user_id, year, month, table_name, id_name)
    
    if monthly_total:
        time = monthly_total[0][0]
        print(f"{user}: {time} h ")

def summarize_week():
    pass

def get_weekly_summary():
    pass