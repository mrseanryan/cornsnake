import logging
import os

from . import config
from . import util_color

# ref https://realpython.com/python-logging/
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def set_log_dir_and_get_path_to_logfile(log_dir):
    path_to_logfile = os.path.join(log_dir, config.LOG_FILENAME)
    logging.basicConfig(filename=path_to_logfile, filemode='w', format=log_format, level=config.LOGGING_LEVEL)
    return path_to_logfile

# Call from inside a Try..Except:
def log_exception(e):
    # do NOT call util_print here (could be infinite loop)
    print(util_color.ERROR_COLOR + "!EXCEPTION!", e, util_color.END_COLORS)
    logging.error("Exception occurred", exc_info=True)  # exc_info=True will auto-log any stack trace

# Call like this: getLogger(__name__) - then we know where did those log entries come from.
def getLogger(name_of_module):
    return logging.getLogger(name_of_module)
