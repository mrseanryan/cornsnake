"""
Working with directories, files, and file paths.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_dir.html)
"""

import os
from glob import glob
import re
import shutil
from pathlib import Path

from . import util_os

TOTAL_BYTES_IN_GIGABYTE = 1000000000


def copy_directory(from_path, to_path):
    """
    Copy a directory from one location to another.

    Args:
    from_path (str): The path of the directory to copy from.
    to_path (str): The path of the directory to copy to.
    """
    shutil.copytree(from_path, to_path)


def ensure_dir_exists(temp_git_fixer_dir):
    """
    Ensure that a directory exists, creating it if necessary.

    Args:
    temp_git_fixer_dir (str): The path of the directory to ensure existence of.
    """
    if not os.path.exists(temp_git_fixer_dir):
        os.makedirs(temp_git_fixer_dir)


def find_files_by_extension(dir_path, extension):
    """
    Find files in a directory by a specific file extension.

    Args:
    dir_path (str): The path of the directory to search for files.
    extension (str): The file extension to search for.

    Returns:
    list: A list of file paths with the specified extension.
    """
    found_files = []
    contents = os.listdir(dir_path)
    for content in contents:
        path_to_sub = os.path.join(dir_path, content)
        if os.path.isfile(path_to_sub) and path_to_sub.endswith(extension):
            found_files.append(path_to_sub)
    return found_files


def find_files(dir_path):
    """Find all files in the given directory."""
    found_files = []
    contents = os.listdir(dir_path)
    for content in contents:
        path_to_sub = os.path.join(dir_path, content)
        if os.path.isfile(path_to_sub):
            found_files.append(path_to_sub)
    return found_files


def find_files_recursively(dir_path, extension=".*"):
    result = [
        y for x in os.walk(dir_path) for y in glob(os.path.join(x[0], f"*{extension}"))
    ]
    return result


def get_dir_parts(path_to_file):
    """
    Get the directory components of the given file path.

    Example: 'c:\\temp\\x\\my-file.txt' -> ['c','temp','x']
    """
    path_to_dir = os.path.dirname(path_to_file)
    path = os.path.normpath(path_to_dir)
    return path.split(os.sep)


def get_directory_of_this_script(____file__):
    """
    Get the directory that contains this script.

    Args:
    __file__ (str): The path to this Python script file.
    Returns:
    The absolute path to directory containing your Python script file.
    """
    return os.path.dirname(os.path.realpath(____file__))


def get_parent_dir(my_path):
    """Get the absolute path of the parent directory of the given directory."""
    return Path(my_path).parent.absolute()


def get_total_dir_size_in_bytes(start_path):
    total_size = 0
    for dirpath, _dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                fp_allow_long_path = "\\\\?\\" + fp if util_os.is_windows() else fp
                total_size += os.path.getsize(fp_allow_long_path)

    return total_size


def get_total_dir_size_in_gigabytes(start_path):
    """Calculate the total size of a directory in gigabytes.
    Args:
    start_path (str): The path of the directory to calculate size of.
    Returns:
    float: The total size of the directory in gigabytes."""
    return get_total_dir_size_in_bytes(start_path) / TOTAL_BYTES_IN_GIGABYTE


def get_unique_dirpath(path_to_dir):
    """
    Get a unique directory path similar to the given path.
    """

    def _ends_with_hyphen_number(path):
        m = re.search(r"-\d+$", path)
        return m is not None

    # Avoid appending like x-01-02-03
    if _ends_with_hyphen_number(path_to_dir):
        path_to_dir = path_to_dir[:-3]

    suffix = 2
    path_to_dir_new = path_to_dir
    while os.path.exists(path_to_dir_new):
        path_to_dir_new = f"{path_to_dir}-{suffix:02}"
        suffix += 1
    return path_to_dir_new


def is_empty_directory(path_to_file):
    """Check if a directory is empty.
    Args:
    path_to_file (str): The path of the directory to check.
    Returns:
    bool: True if the directory is empty, False otherwise."""
    if os.path.isfile(path_to_file):
        return False
    contents = os.listdir(path_to_file)
    return len(contents) == 0


def is_empty_directory_only_subdirectories(path_to_file):
    """Check if a directory is empty by inspecting subdirectories.
    Args:
    path_to_file (str): The path of the directory to check.
    Returns:
    bool: True if the directory is empty or only contains empty subdirectories, False otherwise."""
    if os.path.isfile(path_to_file):
        return False
    contents = os.listdir(path_to_file)
    for content in contents:
        path_to_sub = os.path.join(path_to_file, content)
        if os.path.isfile(path_to_sub):
            return False
        if not os.path.isfile(path_to_sub):
            is_empty = is_empty_directory_only_subdirectories(path_to_sub)
            if not is_empty:
                return False
    return True


def move_directory(path_to_dir, path_to_dir_renamed):
    shutil.move(path_to_dir, path_to_dir_renamed)
