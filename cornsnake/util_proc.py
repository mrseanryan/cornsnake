"""
Running processes and opening Windows Explorer at a specified directory.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_proc.html)
"""

import os
import subprocess

from . import config
from . import util_log
from . import util_os

logger = util_log.getLogger(__name__)


def _proc_print(message: str) -> None:
    """
    Logs the message using the logger and prints it if config.IS_VERBOSE is True.

    Args:
    message (str): The message to log and possibly print.
    """
    logger.info(message)
    if config.IS_VERBOSE:
        print(message)


def _proc_print_debug(message: str) -> None:
    """
    Logs the message at debug level using the logger and prints it if config.IS_VERBOSE is True.

    Args:
    message (str): The message to log and possibly print.
    """
    logger.debug(message)
    if config.IS_VERBOSE:
        print(message)


def is_process_running(process_name: str) -> bool:
    """
    Checks if the given process (identified by program filename) is running.

    Args:
    process_name (str): The filename of the process. For example 'notepad.exe'.
    """
    if util_os.is_windows():
        progs = str(subprocess.check_output("tasklist"))
        return process_name in progs
    else:
        try:
            progs = str(subprocess.check_output(["pgrep", process_name]))
            return process_name in progs
        except subprocess.CalledProcessError:
            return False


def run_process_and_get_output(
    path_to_proc: str,
    arguments: list[str],
    working_directory: str,
    output_errors: bool = True,
    raise_if_str_error: bool = False,
) -> str:
    """
    Executes a process with specified arguments and working directory, capturing the output.

    Args:
    path_to_proc (str): The path to the process to execute.
    arguments (list): List of arguments for the process.
    working_directory (str): The working directory for the process.
    output_errors (bool): Flag to print out errors. Default is True (but only if config.IS_VERBOSITY).
    raise_if_str_error (bool): Flag to raise an exception if stderr was a non-empty string (useful for programs that return 0 exit code, even though they populated stderr). Default is False.

    Returns:
    str: The standard output of the process.

    Raises:
    RuntimeError: If the process returns a non-zero exit code.
    """
    _proc_print_debug(
        f"EXECUTING: '{path_to_proc} {arguments}' - at {working_directory}"
    )

    pipes = subprocess.Popen(
        [path_to_proc] + arguments,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=working_directory,
    )
    std_out, std_err = pipes.communicate()

    std_out_str = ""
    if isinstance(std_out, str):
        std_out_str = std_out
    else:
        std_out_str = std_out.decode()

    std_err_str = ""
    if isinstance(std_err, str):
        std_err_str = std_err
    else:
        std_err_str = std_err.decode()

    if pipes.returncode != 0:
        # an error happened!
        err_msg = f"{std_err_str.strip()}. Code: {pipes.returncode}"
        if output_errors:
            print(err_msg)
        else:
            logger.debug(err_msg)
        raise RuntimeError(err_msg, pipes.returncode)
    elif len(std_err_str):
        # return code is 0 (no error), but we may want to
        # do something with the info on std_err
        if output_errors:
            print(std_err_str)
        else:
            logger.debug(std_err_str)
        if raise_if_str_error:
            err_msg = f"{std_err_str.strip()}. Code: {pipes.returncode}"
            raise RuntimeError(err_msg, pipes.returncode)

    _proc_print_debug(f" >>> {std_out_str}")

    return std_out_str


def open_windows_explorer_at(path_to_dir: str) -> None:
    """
    Opens Windows Explorer or Mac Finder at the specified directory if the OS is Windows.

    Args:
    path_to_dir (str): The path to the directory to open in Windows Explorer.
    """
    if util_os.is_windows():
        _proc_print(f"Opening Explorer at {path_to_dir}")
        os.startfile(path_to_dir)
        return
    if util_os.is_mac():
        _proc_print(f"Opening Finder at {path_to_dir}")
        os.system(f"open {path_to_dir}")
        return
    else:
        _proc_print(f"NOT opening {path_to_dir} - not Windows OS and not Mac")
