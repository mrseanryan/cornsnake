"""
File operations including copying, reading, and writing text to files.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_file.html)
"""

import os
import shutil

from . import util_os
from . import util_pdf
from . import util_text

def copy_file(from_path, to_path):
    """
    Copy a file from one path to another.

    Args:
    from_path (str): The path of the file to copy.
    to_path (str): The destination path to copy the file to.
    """
    shutil.copyfile(from_path, to_path)

def get_this_script_dir(this_file):
    """
    Get the directory of the current script file.

    Args:
    this_file (str): The path of the current script file (__file__).

    Returns:
    str: The directory of the current script file.
    """
    return os.path.dirname(os.path.realpath(this_file))

def _get_long_file_path(path_to_file):
    """
    Get the long file path for Windows.

    Args:
    path_to_file (str): The original file path.

    Returns:
    str: The long file path for Windows.
    """
    return u"\\\\?\\" + path_to_file if util_os.is_windows() else path_to_file

def is_empty_directory_only_subdirectories(path_to_file):
    """
    Check if a directory is empty (only subdirectories are empty).

    Args:
    path_to_file (str): The path to the directory to check.

    Returns:
    bool: True if the directory is empty, False otherwise.
    """
    if os.path.isfile(path_to_file):
        return is_empty_file(path_to_file)
    contents = os.listdir(path_to_file)
    for content in contents:
        path_to_sub = os.path.join(path_to_file, content)
        if os.path.isfile(path_to_sub):
            return is_empty_file(path_to_sub)
        if not os.path.isfile(path_to_sub):
            is_empty = is_empty_directory_only_subdirectories(path_to_sub)
            if not is_empty:
                return False
    return True

def is_empty_file(path_to_file):
    """
    Check if a file is empty.

    Args:
    path_to_file (str): The path to the file to check.

    Returns:
    bool: True if the file is empty, False otherwise.
    """
    if not os.path.isfile(path_to_file):
        return False
    if os.path.islink(path_to_file):
        return False
    fp_allow_long_path = _get_long_file_path(path_to_file)
    size = os.path.getsize(fp_allow_long_path)
    return size == 0

def read_lines_from_file(filepath, skip_comments=False):
    """
    Read lines from a text file.

    Args:
    filepath (str): The path to the text file.
    skip_comments (bool): Whether to skip lines starting with '#'. Default is False.

    Returns:
    list: A list of lines read from the file.
    """
    lines = []
    with open(filepath, encoding='utf-8') as file:
        lines = [line.strip() for line in file]
    if skip_comments:
        lines = _remove_comments(lines)
    return lines

def read_text_from_file(filepath):
    """
    Read text from a text file.

    Args:
    filepath (str): The path to the text file.

    Returns:
    str: The text read from the file.
    """
    with open(filepath, encoding='utf-8') as file:
        return file.read()

def _remove_comments(lines):
    """
    Remove lines starting with '#' from a list of lines.

    Args:
    lines (list): List of lines to filter.

    Returns:
    list: Filtered list of lines without comments.
    """
    filtered_lines = []
    for line in lines:
        if not line.startswith('#'):
            filtered_lines.append(line)
    return filtered_lines

def read_text_from_text_or_pdf_file_skipping_comments(filepath):
    """
    Read text from a text or PDF file, skipping comments.

    Args:
    filepath (str): The path to the text or PDF file.

    Returns:
    str: The text read from the file without comments.
    """
    if util_pdf.is_pdf(filepath):
        return util_pdf.extract_text_from_pdf(filepath)
    lines = read_lines_from_file(filepath)
    filtered_lines = _remove_comments(lines)
    return util_text.LINE_END.join(filtered_lines)

def write_text_lines_to_file(lines, filepath):
    """
    Write lines of text to a text file.

    Args:
    lines (list): List of lines to write to the file.
    filepath (str): The path to the output text file.
    """
    with open(filepath, encoding='utf-8', mode='w') as file:
        for line in lines:
            file.write(line + util_text.LINE_END)

def write_array_to_file_skipping_empty(PATH_TO_OUTPUT_TEXT_FILE, lines):
    """
    Write non-empty lines from an array to a file, skipping empty lines.

    Args:
    PATH_TO_OUTPUT_TEXT_FILE (str): The path to the output text file.
    lines (list): List of lines to write to the file.
    """
    with open(PATH_TO_OUTPUT_TEXT_FILE, 'w') as f:
        for line in lines:
            if line is not None and len(line) > 0:
                f.write(line + '\n')

def write_text_to_file(text, filepath):
    """
    Write text to a text file.

    Args:
    text (str): The text to write to the file.
    filepath (str): The path to the output text file.
    """
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(text)

def get_last_part_of_path(file_path):
    """
    Get the last part of a file path (filename).

    Args:
    file_path (str): The full file path.

    Returns:
    str: The last part of the file path (filename).
    """
    return file_path.split(os.sep)[-1]
