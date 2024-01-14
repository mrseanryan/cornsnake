# Single print entry point - so can add color and logging.

from . import util_color
from . import util_log

logger = util_log.getLogger(__name__)

def print_custom(text):
    print(text)
    logger.info(text)

def print_custom_with_logger(text, given_logger):
    print(text)
    given_logger.info(text)

def print_with_color(text, color):
    print_custom(util_color.colorize(text, color))

def print_error(message):
    print_with_color(message, util_color.ERROR_COLOR)

def print_important(text):
    print_with_color(text, util_color.IMPORTANT)

def _print_section(title, color, section_id):
    print_with_color(f"=== === ===\t[{section_id}] {title}\t=== === ===", color)

test_section_id = 1
def print_test_section(title):
    global test_section_id
    _print_section(title, util_color.TEST_SECTION_COLOR, test_section_id)
    test_section_id += 1

section_id = 1
def print_section(title, color=util_color.SECTION_COLOR, _section_id=None):
    global section_id
    _section_id = _section_id if _section_id is not None else section_id
    print_with_color(f"=== === ===\t[{section_id}] {title}\t=== === ===", color)
    section_id += 1

def reset_section_count():
    global section_id
    section_id = 1

def print_result(text):
    print_with_color(text, util_color.RESULT_COLOR)

def print_warning(text):
    print_with_color("WARNING: " + text, util_color.WARNING_COLOR)
