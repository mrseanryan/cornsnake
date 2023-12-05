import config

import subprocess

def run_process_and_get_output(path_to_proc, arguments, working_directory):
    if config.IS_VERBOSE:
        print(f"EXECUTING: '{path_to_proc} {arguments}' - at {working_directory}")
    result = subprocess.run([path_to_proc] + arguments, stdout=subprocess.PIPE, check=True, text=True, cwd=working_directory).stdout
    if config.IS_VERBOSE:
        print(f" >>> {result}")
    return result
