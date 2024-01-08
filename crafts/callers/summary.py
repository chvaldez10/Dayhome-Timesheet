from emailer.email_sender import EmailSender
from readers.json_reader import load_json
from utilities.date_time_utilities import format_year_month_day
from summarizer.summary_manager import SummaryManager

USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def summarizer(provider_id:str, year: int, month: int, day: int, mode: str) -> None:
    formatted_year_month_day = format_year_month_day(year, month, day)
    my_email_sender = EmailSender(formatted_year_month_day, "Gmail", "email_template_day.html")
    summary_manager = SummaryManager(provider_id, year, month, day)

    # summarize day
    if mode == "daily":
        user_data = summary_manager.summarize_day()
        my_email_sender.user_data = user_data
        my_email_sender.send_email(f"Summary for {formatted_year_month_day} 🏠")
    elif mode == "weekly":
        pass
    elif mode == "monthly":
        user_data = summary_manager.summarize_month()
        print("user data: ", user_data)