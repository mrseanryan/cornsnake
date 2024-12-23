"""
Decorators for your Python code.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/decorators.html)
"""

from typing import Any, Callable
from . import util_log
from . import util_time

logger = util_log.getLogger(__name__)


def timer(original_function: Callable) -> Any:
    """
    Adds a timer to your function - prints out the time taken, to the console and writes to log.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = util_time.start_timer()

        # Call the original function
        result = original_function(*args, **kwargs)

        elapsed = util_time.end_timer(start)
        message = f"[time taken: {util_time.describe_elapsed_seconds(elapsed)}]"
        print(message)
        logger.info(message)

        return result

    return wrapper
