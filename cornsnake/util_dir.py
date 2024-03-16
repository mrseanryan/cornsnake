"""
Working with directories, files, and file paths.
"""

import os
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
    found_files = []
    contents = os.listdir(dir_path)
    for content in contents:
        path_to_sub = os.path.join(dir_path, content)
        if os.path.isfile(path_to_sub):
            found_files.append(path_to_sub)
    return found_files

def get_directory_of_this_script():
    return os.path.dirname(os.path.realpath(__file__))

def get_parent_dir(my_path):
    return Path(my_path).parent.absolute()

def get_total_dir_size_in_bytes(start_path):
    total_size = 0
    for dirpath, _dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                fp_allow_long_path = u"\\\\?\\" + fp if util_os.is_windows() else fp
                total_size += os.path.getsize(fp_allow_long_path)

    return total_size

def get_total_dir_size_in_gigabytes(start_path):
    return get_total_dir_size_in_bytes(start_path) / TOTAL_BYTES_IN_GIGABYTE

def is_empty_directory(path_to_file):
    if os.path.isfile(path_to_file):
        return False
    contents = os.listdir(path_to_file)
    return len(contents) == 0

def is_empty_directory_only_subdirectories(path_to_file):
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

def write_text_to_file(text, filepath):
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(text)
