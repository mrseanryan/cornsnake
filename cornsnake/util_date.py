"""
Functions for date manipulation. It includes functions to parse, format, add days to, and validate dates in the yyyy-mm-dd format.
"""

from datetime import datetime, timedelta
import re

def parse_yyyy_mm_dd(arg_date):
    """
    Parse a date string in the yyyy-mm-dd format to a datetime object.

    Args:
    arg_date (str): Date string in the format yyyy-mm-dd.

    Returns:
    datetime: Datetime object representing the parsed date.
    """
    return datetime.strptime(arg_date, "%Y-%m-%d")

def _date_to_yyyy_mm_dd(arg_date):
    """
    Format a datetime object to a date string in the yyyy-mm-dd format.

    Args:
    arg_date (datetime): Datetime object to format.

    Returns:
    str: Date string in the format yyyy-mm-dd.
    """
    return arg_date.strftime("%Y-%m-%d")

def add_day_to_date(str_date, days):
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

def is_valid_date_yyyy_mm_dd(value):
    """
    Check if a date string is in the valid yyyy-mm-dd format.

    Args:
    value (str): Date string to validate.

    Returns:
    bool: True if the date string is in the correct format, False otherwise.
    """
    pat = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
    return re.fullmatch(pat, value)
