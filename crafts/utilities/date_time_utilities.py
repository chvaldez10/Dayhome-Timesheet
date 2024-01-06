from datetime import timedelta, datetime

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