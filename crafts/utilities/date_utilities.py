import re
from datetime import datetime
from exceptions.date_parsing_error import DateParsingError

DATE_PATTERN = r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"


def parse_for_valid_date(date_string: str):
    """
    Parse the provided string for a valid date.

    Args:
        date_string (str): The string containing the date.

    Returns:
        datetime.date: The extracted date object.

    Raises:
        DateParsingError: If no valid date is found.
    """
    date_match = re.search(DATE_PATTERN, date_string)
    if date_match:
        date_str = date_match.group(0)

        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise DateParsingError(f"Invalid date format: {date_str}")
    raise DateParsingError("No matched date.")