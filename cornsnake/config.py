"""Globally accessible config object. Can be configured by for example reading from command line arguments or TOML file (via tomllib), and then writing to the properties in-memory.

- see util_toml.py for an example of reading from an ini file (TOML format).

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/config.html)
"""

import logging

IS_VERBOSE = False
PATH_TO_GIT = r"C:\Program Files\Git\cmd\git.exe"

path_to_repo_dir = r"C:\src\github\my-repo"
date_param = "2023-06-01"
branches = ["main"]
file_extensions = ""  # ".log,.zip,.js.map"

blob_size = "512K"

# SYSTEM CONFIG
IS_COLOR_ENABLED = True
IS_INTERACTIVE = (
    True  # Normally True. Set to False for 'hands free' mode for automation
)
LOGGING_LEVEL = logging.INFO
LOG_FILENAME = "my-log.log"
MINIMIZE_PROGRESS_BAR_OUTPUT = (
    False  # Normally False. Set to True for CI/CD build or other log-first environment.
)
