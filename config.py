import logging

IS_VERBOSE = False
PATH_TO_GIT = r"C:\Program Files\Git\cmd\git.exe"

path_to_repo_dir = r'C:\MxApps\git-fix-apps\t2\6aaf3500-ea19-464e-b1fd-cca4baa3660f'
date_param = '2023-06-01'
branches = ['main']
file_extensions = "" # ".log,.zip,.js.map"

blob_size = "512K"

# SYSTEM CONFIG
IS_COLOR_ENABLED = True
IS_INTERACTIVE = False # Normally True. Set to False for 'hands free' mode for automation
LOGGING_LEVEL = logging.INFO
LOG_FILENAME = 'my-log.log'
