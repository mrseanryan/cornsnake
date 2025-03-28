"""
Functions for date manipulation. It includes functions to parse, format, add days to, and validate dates in the yyyy-mm-dd format.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_date.html)
"""

from datetime import datetime, timedelta, timezone
import re


def parse_yyyy_mm_dd(arg_date: str) -> datetime:
    """
    Parse a date string in the yyyy-mm-dd format to a datetime object.

    Args:
    arg_date (str): Date string in the format yyyy-mm-dd.

    Returns:
    datetime: Datetime object representing the parsed date.
    """
    return datetime.strptime(arg_date, "%Y-%m-%d")


def _date_to_yyyy_mm_dd(arg_date: datetime) -> str:
    """
    Format a datetime object to a date string in the yyyy-mm-dd format.

    Args:
    arg_date (datetime): Datetime object to format.

    Returns:
    str: Date string in the format yyyy-mm-dd.
    """
    return arg_date.strftime("%Y-%m-%d")


def add_day_to_date(str_date: str, days: int) -> str:
    """
    Add a specified number of days to a date string in the yyyy-mm-dd format.

    Args:
    str_date (str): Date string in the format yyyy-mm-dd.
    days (int): Number of days to add to the date.

    Returns:
    str: Date string in the format yyyy-mm-dd after adding the specified days.
    """
    date_value = parse_yyyy_mm_dd(str_date)
    date_value += timedelta(days)
    return _date_to_yyyy_mm_dd(date_value)


def is_valid_date_yyyy_mm_dd(value: str) -> bool:
    """
    Check if a date string is in the valid yyyy-mm-dd format.

    Args:
    value (str): Date string to validate.

    Returns:
    bool: True if the date string is in the correct format, False otherwise.
    """
    pat = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
    return True if re.fullmatch(pat, value) else False


def get_now_for_system_timezone() -> datetime:
    """
    Get the current date and time, for the system timezone.

    Returns:
    datetime: Date and time for the system timezone.
    """
    return datetime.now(timezone.utc).astimezone()
