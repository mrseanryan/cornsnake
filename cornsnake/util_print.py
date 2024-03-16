"""
A Single entry point for printing - so can add custom printing with color and logging.

Functions for printing with different colors, logging messages, printing sections, and handling warnings.
"""

from . import util_color
from . import util_log

logger = util_log.getLogger(__name__)

def percent(num, denom, ndigits=0):
    """
    Calculate the percentage of two numbers.

    Args:
    num (int): The numerator.
    denom (int): The denominator.
    ndigits (int): Number of digits after the decimal point. Default is 0.

    Returns:
    str: The percentage as a string.
    """
    if denom == 0:
        return format(0, f'.{ndigits}f')
    return str(round((num * 100.0) / denom, ndigits)) + '%'

def print_no_endline(text):
    """
    Print text without a newline character and log the message.

    Args:
    text (str): The text to print.
    """
    print(text, end='')
    logger.info(text)

def print_custom(text):
    """
    Print text with a newline character and log the message.

    Args:
    text (str): The text to print.
    """
    print(text)
    logger.info(text)

def print_custom_with_logger(text, given_logger):
    """
    Print text with a newline character using a specific logger.

    Args:
    text (str): The text to print.
    given_logger: The logger to use.
    """
    print(text)
    given_logger.info(text)

def print_with_color(text, color):
    """
    Print text with a specified color.

    Args:
    text (str): The text to print.
    color (str): The color to apply.
    """
    print_custom(util_color.colorize(text, color))

def print_error(message):
    """
    Print an error message with a specific color.

    Args:
    message (str): The error message to print.
    """
    print_with_color(message, util_color.ERROR_COLOR)

def print_important(text):
    """
    Print important text with a specific color.

    Args:
    text (str): The important text to print.
    """
    print_with_color(text, util_color.IMPORTANT)

def _print_section(title, color, section_id):
    """
    Print a section title with a specific color and section ID.

    Args:
    title (str): The title of the section.
    color (str): The color of the section.
    section_id (int): The ID of the section.
    """
    print_with_color(f"=== === ===\t[{section_id}] {title}\t=== === ===", color)

test_section_id = 1
def print_test_section(title):
    """
    Print a test section with a specific color.

    Args:
    title (str): The title of the test section.
    """
    global test_section_id
    _print_section(title, util_color.TEST_SECTION_COLOR, test_section_id)
    test_section_id += 1

section_id = 1
def print_section(title, color=util_color.SECTION_COLOR, _section_id=None):
    """
    Print a section with a specific color and section ID.

    Args:
    title (str): The title of the section.
    color (str): The color of the section. Default is util_color.SECTION_COLOR.
    _section_id (int): The ID of the section. Default is None.
    """
    global section_id
    _section_id = _section_id if _section_id is not None else section_id
    print_with_color(f"=== === ===\t[{section_id}] {title}\t=== === ===", color)
    section_id += 1

def reset_section_count():
    """
    Reset the section count back to 1.
    """
    global section_id
    section_id = 1

def print_result(text):
    """
    Print a result message with a specific color.

    Args:
    text (str): The result message to print.
    """
    print_with_color(text, util_color.RESULT_COLOR)

def print_warning(text):
    """
    Print a warning message with a specific color.

    Args:
    text (str): The warning message to print.
    """
    print_with_color("WARNING: " + str(text), util_color.WARNING_COLOR)
