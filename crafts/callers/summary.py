from emailer.email_sender import EmailSender
from readers.json_reader import load_json
from utilities.date_time_utilities import format_year_month_day
from summarizer.summary_manager import SummaryManager
from utilities.calendar_df_utilities import format_calendar_df

USER_FILENAME = "./json/users.json"
MONTH_MAP_FILENAME = "./json/month_map.json"

USER_ID_MAP = load_json(USER_FILENAME)
MONTH_MAP = load_json(MONTH_MAP_FILENAME)

def summarizer(provider_id:str, year: int, month: int, day: int, mode: str) -> None:
    formatted_year_month_day = format_year_month_day(year, month, day)
    my_email_sender = EmailSender(formatted_year_month_day, "Gmail")
    summary_manager = SummaryManager(provider_id, year, month, day)

    # summarize day
    if mode == "daily":
        user_data = summary_manager.summarize_day()
        my_email_sender.user_data = user_data
        my_email_sender.template_file = "email_template_day.html"
        my_email_sender.send_email(f"Summary for {formatted_year_month_day} 🏠")
    elif mode == "weekly":
        user_data = summary_manager.summarize_week()
        restructured_data = format_calendar_df(user_data)
        # print(restructured_data["Alanna Ahmed"][1]["In"])
        my_email_sender.user_data = restructured_data
        my_email_sender.template_file = "email_template_week.html"
        my_email_sender.send_email(f" {MONTH_MAP[str(month)]} {year} overview 🗓️")
    elif mode == "monthly":
        user_data = summary_manager.summarize_month()
        my_email_sender.user_data = user_data
        my_email_sender.template_file = "email_template_month.html"
        my_email_sender.send_email(f"Summary for {MONTH_MAP[str(month)]} {year} 🏠")

    print("Email sent.")