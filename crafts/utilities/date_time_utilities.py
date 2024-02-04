from datetime import timedelta, datetime
import calendar

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

def find_start_of_week(year: int, month: int) -> datetime:
    """
    Finds the first Monday of the specified month and year, adjusting for underflow if necessary.

    Monday is the chosen start of week.
    """
    first_day_of_month = datetime(year, month, 1)
    first_weekday = first_day_of_month.weekday()
    days_until_first_monday = (7 - first_weekday) % 7
    first_monday = first_day_of_month + timedelta(days=days_until_first_monday)
    
    # Correct for underflow
    if first_weekday != calendar.MONDAY:
        first_monday -= timedelta(days=7)
    return max(first_monday, first_day_of_month)

def find_friday_of_the_week(start_of_week: datetime, year: int, month: int) -> datetime:
    """
    Find the friday of the week
    """
    friday_of_week = start_of_week + timedelta(days=4)

    if friday_of_week.month != month:  # Correct for overflow
        friday_of_week = datetime(year, month, calendar.monthrange(year, month)[1])

    return friday_of_week

def generate_week_day_ranges(first_monday: datetime, year: int, month: int) -> dict:
    """
    Generates a dictionary with week numbers as keys and date ranges for Mondays to Fridays as values, starting from the given first Monday of the month.
    """
    current_monday = first_monday
    week_day_range = {}
    week_number = 1
    
    while current_monday.month == month:
        friday_of_week = find_friday_of_the_week(first_monday, year, month)
        
        day_range_str = f"{current_monday.day}-{friday_of_week.day}"
        week_day_range[week_number] = day_range_str
        week_number += 1
        current_monday += timedelta(days=7)
    
    return week_day_range

def get_week_day_range(year: int, month: int) -> dict:
    """
    Get a week day range for a given year and month, returning a dictionary with
    week numbers as keys and strings representing the day range of Mondays to Fridays
    within each week as values.
    """
    first_monday = find_start_of_week(year, month)
    week_day_range = generate_week_day_ranges(first_monday, year, month)
    return week_day_range