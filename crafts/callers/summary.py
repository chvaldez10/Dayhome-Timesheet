from emailer.email_sender import EmailSender
from readers.json_reader import load_json
from utilities.date_time_utilities import format_year_month_day
from summarizer.summary_manager import SummaryManager

USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def summarizer(provider_id:str, year: int, month: int, day:int) -> None:
    formatted_year_month_day = format_year_month_day(year, month, day)
    my_email_sender = EmailSender(formatted_year_month_day, "Gmail")
    summary_manager = SummaryManager(provider_id, year, month, day)

    # summarize day
    user_data = summary_manager.summarize_day()
    my_email_sender.user_data = user_data
    my_email_sender.send_email(f"Summary for {formatted_year_month_day} 🏠")

    # summarize_month(provider_id, year, month, day)

# def summarize_month(provider_id: str, year: int, month: int, day:int) -> None:
#     print(f"\nMonthly Summary for {year}/{month}/{day}\n" + "="*50)
#     get_monthly_summary("Me", provider_id, year, month, day, "ProviderLog", "ProviderID")
#     for user, user_id in USER_ID_MAP.items():
#         get_monthly_summary(user, user_id, year, month, day, "DailyLog", "ChildrenID")

# def get_monthly_summary(user: str, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str) -> None:
#     my_database = MySQLDatabase()
#     monthly_total = query_for_monthly_total(my_database, user_id, year, month, table_name, id_name)
    
#     if monthly_total:
#         time = monthly_total[0][0]
#         print(f"{user}: {time} h ")

# def summarize_week():
#     pass

# def get_weekly_summary():
#     pass