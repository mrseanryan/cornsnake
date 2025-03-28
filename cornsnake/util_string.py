"""
Functions for working with strings: filtering by regex, checking if is mostly empty, replacing whilst maintaining casing.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_string.html)
"""

import re


def filter_string_via_regex(text: str, regex: str, replacement_char: str) -> str:
    """
    Filter the given string, to only characters that match the given regex.
      - characters that do not match are replaced with 'replacement_char'

    Example: filter_string_via_regex("this is a test 123 !@#", "_") -> "this_is_a_test_123____"
    """

    def _is_ok(c: str) -> bool:
        return True if re.match(regex, c) else False

    def _process_char(c: str) -> str:
        return c if _is_ok(c) else replacement_char

    return "".join([_process_char(c) for c in text])


def is_empty(text: str) -> bool:
    """
    Function to check if a text string is empty or '-'.

    Args:
    text (str): The text string to check.

    Returns:
    bool: True if the text is empty (None or contains only whitespace or a hyphen), False otherwise.
    """
    if text is None:
        return True
    stripped = text.strip()
    return stripped == "" or stripped == "-"


def replace_keep_case(word__for_regex: str, replacement: str, text: str) -> str:
    """
    Replace ocurrences of 'word__for_regex' in 'text', with 'replacement', trying to maintain the same casing.

    - supports lower, titla and upper casing
    """

    def func(match: re.Match[str]) -> str:
        g = match.group()
        if g.islower():
            return replacement.lower()
        if g.istitle():
            return replacement.title()
        if g.isupper():
            return replacement.upper()
        return replacement

    return re.sub(word__for_regex, func, text, flags=re.I)


def split_into_lines(text: str, max_length: int = 200) -> list[str]:
    """
    Split text into lines of maximum length at word boundaries.

    Args:
        text (str): Text to split
        max_length (int): Maximum line length (default: 200)

    Returns:
        list: List of lines
    """
    if not text:
        return []

    result = []
    current_line = ""

    for word in text.split():
        # Check if adding word would exceed max_length
        if len(current_line) + len(word) + (1 if current_line else 0) <= max_length:
            # Add word with a space if not the first word
            current_line += " " + word if current_line else word
        else:
            # Line would be too long, start a new one
            result.append(current_line)
            current_line = word

    # Add the last line if it has content
    if current_line:
        result.append(current_line)

    return result
