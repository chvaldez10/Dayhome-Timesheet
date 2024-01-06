from datetime import timedelta

def format_timedelta_as_hhmm_ampm(td: timedelta):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return "{:02d}:{:02d} {}".format(hours, minutes, "AM" if hours < 12 else "PM")