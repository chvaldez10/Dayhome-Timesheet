from datetime import timedelta, datetime
import calendar
from itertools import zip_longest
from typing import List, Tuple

def format_timedelta_as_hhmm_ampm(td: timedelta) -> str:
    """
    Format time in 12 hour format: {[1-12]}:{[0-59]} AM/PM.
    """
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
    """
    Format year month day to: Month Day, Year.
    """
    date_str = f"{year}-{month:02d}-{day:02d}"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
    return formatted_date

def get_first_weekday_of_month(year: int, month: int) -> datetime:
    """
    Finds the first day of the specified month.
    Monday is the chosen start of week.
    """
    first_day_of_month = datetime(year, month, 1)
    while first_day_of_month.weekday() >= 5:
        first_day_of_month += timedelta(days=1)

    return first_day_of_month

def get_all_mondays_of_month(year: int, month: int) -> list:
    """
    Return a list of all Mondays of the specified month and year.
    """
    first_day = datetime(year, month, 1)
    first_day_weekday = first_day.weekday()
    days_until_first_monday = (7 - first_day_weekday) % 7
    first_monday = first_day + timedelta(days=days_until_first_monday)
    mondays = [first_monday]
    next_monday = first_monday + timedelta(days=7)
    
    while next_monday.month == month:
        mondays.append(next_monday)
        next_monday += timedelta(days=7)
    
    return mondays

def get_last_weekday_of_month(year: int, month: int) -> datetime:
    """
    Find the last weekday (Monday to Friday) of the specified month and year.
    """
    # Get the last day of the month
    last_day = calendar.monthrange(year, month)[1]
    last_date = datetime(year, month, last_day)
    
    while last_date.weekday() >= 5:
        last_date -= timedelta(days=1)
    
    return last_date


def get_all_fridays_of_month(year: int, month: int) -> list:
    """
    Return a list of all Fridays of the specified month and year.
    """
    first_day = datetime(year, month, 1)
    first_day_weekday = first_day.weekday()
    days_until_first_friday = (4 - first_day_weekday) % 7
    
    # If the first day of the month is after Friday, adjust for the next week
    if first_day_weekday > 4:
        days_until_first_friday += 7
    
    first_friday = first_day + timedelta(days=days_until_first_friday)
    fridays = [first_friday]
    
    next_friday = first_friday + timedelta(days=7)
    while next_friday.month == month:
        fridays.append(next_friday)
        next_friday += timedelta(days=7)
    
    return fridays

def generate_week_day_map(year: int, month: int) -> List[Tuple[datetime, datetime]]:
    # get all days that would start the week
    first_day = get_first_weekday_of_month(year, month)
    mondays = get_all_mondays_of_month(year, month)

    # get all days that would end the week
    last_day = get_last_weekday_of_month(year, month)
    fridays = get_all_fridays_of_month(year, month)

    # append to the list
    if first_day not in mondays:
        mondays.insert(0, first_day)

    if last_day not in fridays:
        fridays.append(last_day)

    return list(zip_longest(mondays, fridays, fillvalue=None))


def generate_week_day_string(week_day_map: List[Tuple[datetime, datetime]]) -> dict:
    """
    Generates a dictionary with week numbers as keys and date ranges for Mondays to Fridays as values, starting from the given first Monday of the month.
    """
    week_day_range = {}
    week_number = 1
    
    for week_day_item in week_day_map:
        day_range_str = f"__{week_day_item[0].day}__-__{week_day_item[1].day}__"
        week_day_range[week_number] = day_range_str
        week_number += 1

    return week_day_range

def get_week_day_range(year: int, month: int) -> dict:
    """
    Get a week day range for a given year and month, returning a dictionary with
    week numbers as keys and strings representing the day range of Mondays to Fridays
    within each week as values.
    """
    week_day_map = generate_week_day_map(year, month)
    week_day_range = generate_week_day_string(week_day_map)
    return week_day_range