from emailer.email_sender import EmailSender
from readers.json_reader import load_json
from utilities.date_time_utilities import format_year_month_day, get_week_day_range
from utilities.calendar_df_utilities import format_calendar_df, get_formatted_calendar_df_weekly_total
from summarizer.summary_manager import SummaryManager

# Constants
USER_FILENAME = "./json/users.json"
MONTH_MAP_FILENAME = "./json/month_map.json"

# Load global data
USER_ID_MAP = load_json(USER_FILENAME)
MONTH_MAP = load_json(MONTH_MAP_FILENAME)

def send_summary_email(email_sender, subject, template_file, user_data, additional_data=None):
    """ Sends a summary email with the provided data. """
    email_sender.user_data = user_data
    email_sender.template_file = template_file
    email_sender.send_email(subject, additional_data)

def summarizer(provider_id: str, year: int, month: int, day: int, mode: str) -> None:
    """
    Summarizes data based on the given mode and sends an email with the summary.

    :param provider_id: Provider ID for the summary
    :param year: Year for the summary
    :param month: Month for the summary
    :param day: Day for the summary
    :param mode: Mode of summarization ('daily', 'weekly', 'monthly')
    """
    formatted_year_month_day = format_year_month_day(year, month, day)
    my_email_sender = EmailSender(formatted_year_month_day, "Gmail")
    summary_manager = SummaryManager(provider_id, year, month, day)

    if mode == "daily":
        user_data = summary_manager.summarize_day()
        email_subject = f"Summary for {formatted_year_month_day} 🏠"
        send_summary_email(my_email_sender, email_subject, "email_template_day.html", user_data)

    elif mode == "weekly":
        user_data = summary_manager.summarize_week()
        week_range_list = get_week_day_range(year, month)
        restructured_data = format_calendar_df(user_data)
        get_formatted_calendar_df_weekly_total(restructured_data, len(week_range_list))
        email_subject = f"{MONTH_MAP[str(month)]} {year} Overview 🗓️"
        send_summary_email(my_email_sender, email_subject, "email_template_week.html", restructured_data, week_range_list)

    elif mode == "monthly":
        user_data = summary_manager.summarize_month()
        email_subject = f"Summary for {MONTH_MAP[str(month)]} {year} 🏠"
        send_summary_email(my_email_sender, email_subject, "email_template_month.html", user_data)

    print("Email sent.")