from datetime import timedelta, datetime
from typing import List, Tuple
import calendar

def format_timedelta_as_hhmm_ampm(td: timedelta):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours >= 12:
        ampm = "PM"
        if hours > 12:
            hours -= 12
    else:
        ampm = "AM"
        if hours == 0:
            hours = 12

    return f"{hours:02}:{minutes:02} {ampm}"

def format_year_month_day(year:int, month:int, day:int) -> str:
    date_str = f"{year}-{month:02d}-{day:02d}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
    return formatted_date

def get_week_day_range(year: int, month:str) -> List[str]:
    """Get a week day range for a given year and month."""
    # Find the first Monday of the month
    first_day_of_month = datetime(year, month, 1)
    first_monday = first_day_of_month + timedelta(days=(7 - first_day_of_month.weekday() + calendar.MONDAY) % 7)

    # Generate all Mondays of the month
    week_day_range = []
    current_monday = first_monday
    while current_monday.month == month:
        current_monday_day = current_monday.date().day
        temp_date_range_str = f"{current_monday_day}-{current_monday_day+5}"
        week_day_range.append(temp_date_range_str)
        current_monday += timedelta(days=7)

    print(week_day_range)
    return week_day_range