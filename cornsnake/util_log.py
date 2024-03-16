"""
Functions related to logging. It includes functions for setting up logging configuration, logging exceptions, and getting loggers for modules.
"""

import logging
import os

from . import config
from . import util_color

# Define the log format
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def set_log_dir_and_get_path_to_logfile(log_dir):
    """
    Function to set the log directory and get the path to the logfile.

    Args:
    log_dir (str): The directory where the log file will be stored.

    Returns:
    str: The path to the logfile.
    """
    path_to_logfile = os.path.join(log_dir, config.LOG_FILENAME)
    logging.basicConfig(filename=path_to_logfile, filemode='w', format=log_format, level=config.LOGGING_LEVEL)
    return path_to_logfile

def log_exception(e):
    """
    Function to log an exception.

    Args:
    e (Exception): The exception to log.
    """
    print(util_color.ERROR_COLOR + "!EXCEPTION!", e, util_color.END_COLORS)
    logging.error("Exception occurred", exc_info=True)

def getLogger(name_of_module):
    """
    Function to get a logger for a specific module.

    Args:
    name_of_module (str): The name of the module.

    Returns:
    Logger: The logger for the specified module.
    """
    return logging.getLogger(name_of_module)
