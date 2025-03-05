"""
Functions for logging exceptions and setting up logging configurations.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_log.html)
"""

import logging
import os
import re
import typing

from . import config
from . import util_color

# Define the format for log entries
# ref https://realpython.com/python-logging/
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def set_log_dir_and_get_path_to_logfile(log_dir: str) -> str:
    """
    Set the log directory and get the path to the log file.

    Args:
    log_dir (str): The directory where the log file will be stored.

    Returns:
    str: The path to the log file.
    """
    path_to_logfile = os.path.join(log_dir, config.LOG_FILENAME)
    logging.basicConfig(
        filename=path_to_logfile,
        filemode="w",
        format=log_format,
        level=config.LOGGING_LEVEL,
    )
    return path_to_logfile


def log_exception(e: typing.Any) -> None:
    """
    Log an exception.
    -  Call from inside a Try..Except

    Args:
    e (Exception): The exception to be logged.
    """
    # do NOT call util_print here (could be infinite loop)
    print(util_color.ERROR_COLOR + "!EXCEPTION!", e, util_color.END_COLORS)
    logging.exception("Exception occurred")


def getLogger(name_of_module: str) -> logging.Logger:
    """
    Get a logger with the specified name.

    - Call like this: getLogger(__name__) - then we know where did those log entries come from.

    Args:
    name_of_module (str): The name of the module to create the logger for.

    Returns:
    Logger: A logger object for the specified module.
    """
    return logging.getLogger(name_of_module)


MASKED = "<masked>"
pat = re.compile(r".*[/|\\]Users[/|\\]([A-Za-z.]*)[/|\\]{1}.*", re.M)

WINDOWS_SEP = "\\"
MAC_SEP = "/"


def mask_sensitive_text(text: str) -> str:
    """
    Mask text that contains a user name.

    Examples:
    - Windows: C:\\Users\\Bob.Jones\\my-file.txt -> C:\\Users\\<masked>\\my-file.txt
    - Mac: /Users/Bob.Jones/my-file.txt -> /Users/<masked>\\my-file.txt
    """
    try:
        sensitive_win = WINDOWS_SEP + "Users" + WINDOWS_SEP
        sensitive_mac = MAC_SEP + "Users" + MAC_SEP

        if (
            sensitive_win in text or sensitive_mac in text
        ):  # Both can occur with git on Windows
            matches = set(pat.findall(text))

            while matches:
                for m in matches:
                    text = text.replace(m, "<masked>")
                matches = set(pat.findall(text))
    except ValueError:
        pass  # logging code needs to be robust
    except RuntimeError:
        pass  # logging code needs to be robust

    return text


def log_sensitive_info(text: str, logger: logging.Logger) -> None:
    """
    Log at info level, masking out any user name in the text.
    """
    logger.info(mask_sensitive_text(text))


def log_sensitive_warn(text: str, logger: logging.Logger) -> None:
    """
    Log at warn level, masking out any user name in the text.
    """
    logger.warn(mask_sensitive_text(text))
