from datetime import datetime
import re

def parse_yyyy_mm_dd(arg_date):
    return datetime.strptime(arg_date, '%Y-%m-%d')

def is_valid_date_yyyy_mm_dd(value):
    pat = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
    return re.fullmatch(pat, value)
