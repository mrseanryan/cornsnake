"""
File operations including copying, reading, and writing text to files.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_file.html)
"""

import datetime
import os
import shutil

from . import util_os
from . import util_pdf
from . import util_text
from . import util_string


def backup_file_by_copying(
    path_to_file: str, backup_dir: str, backup_filename: str
) -> str:
    """
    Backup the given file by copying it to a new uniquely named file.
    """
    path_to_backup = os.path.join(backup_dir, backup_filename)
    path_to_backup = get_unique_filepath(path_to_backup)
    copy_file(path_to_file, path_to_backup)
    return path_to_backup


def change_extension(input_filename: str, new_extension: str) -> str:
    """
    Change the extension of the given filename.

    Examples:
    - ('input1.txt', '.yaml') -> 'input1.yaml')
    - ('input2', '.yaml.txt') -> 'input2.yaml.txt')
    - ('input3', '.xml') -> 'input3.xml')
    - ('input1.txt.zip', '.zip') -> 'input1.zip')
    """
    if not new_extension.startswith("."):
        raise ValueError("new_extension must start with a '.'. For example: '.txt'")
    base_filename = input_filename
    if "." in input_filename:
        parts = input_filename.split(".")
        base_filename = ".".join(parts[:-1])
    if base_filename.endswith(new_extension):
        return base_filename
    return base_filename + new_extension


def get_file_extension(filename: str, to_lower: bool = True) -> str:
    """Get the extension part of the filename - for example '.txt'."""
    _, extension = os.path.splitext(filename)
    return extension.lower() if to_lower else extension


def remove_file_extension(filename: str) -> str:
    """Remove the extension part of the file name - for example 'my-file.txt' -> 'my-file'."""
    return filename.removesuffix(get_file_extension(filename=filename, to_lower=False))


def make_filename_valid(filename: str) -> str:
    """
    Return an altered filename so that it is valid.
    - the new filename will only have alphanumerics, underscore and full-stop.
    """
    return util_string.filter_string_via_regex(
        text=filename, regex="^[a-zA-Z0-9_\\.]+$", replacement_char="_"
    )


def copy_file(from_path: str, to_path: str) -> None:
    """
    Copy a file from one path to another.

    Args:
    from_path (str): The path of the file to copy.
    to_path (str): The destination path to copy the file to.
    """
    shutil.copyfile(from_path, to_path)


def delete_file(path_to_file: str) -> None:
    """
    Delete a file from the disk.
    """
    os.remove(path_to_file)


def get_modified_date(path_to_file: str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(os.path.getmtime(path_to_file))


def get_unique_filepath(path_to_file: str) -> str:
    """
    Get a unique new filepath, similar to the given path.
    """
    filename_no_extension, extension = os.path.splitext(path_to_file)

    suffix = 2
    while os.path.exists(path_to_file):
        path_to_file = f"{filename_no_extension}-{suffix:02}{extension}"
        suffix += 1
    return path_to_file


def get_this_script_dir(this_file: str) -> str:
    """
    Get the directory of the current script file.

    Args:
    this_file (str): The path of the current script file (__file__).

    Returns:
    str: The directory of the current script file.
    """
    return os.path.dirname(os.path.realpath(this_file))


def is_file_under_dir(path_to_file: str, path_to_dir: str) -> bool:
    """
    Does that file exist under that directory or a sub-directory.
    """
    path_to_file = os.path.normpath(path_to_file)
    path_to_dir = os.path.normpath(path_to_dir) + os.sep
    return path_to_file.startswith(path_to_dir)


def _get_long_file_path(path_to_file: str) -> str:
    """
    Get the long file path for Windows.

    Args:
    path_to_file (str): The original file path.

    Returns:
    str: The long file path for Windows.
    """
    return "\\\\?\\" + path_to_file if util_os.is_windows() else path_to_file


def is_empty_directory_only_subdirectories(path_to_file: str) -> bool:
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


def is_empty_file(path_to_file: str) -> bool:
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


def move_file(from_filepath: str, to_filepath: str) -> None:
    """
    Recursively move a file or directory to another location. This is similar to the Unix "mv" command. Return the file or directory's destination.

    If the destination is a directory or a symlink to a directory, the source is moved inside the directory. The destination path must not already exist.
    """
    shutil.move(from_filepath, to_filepath)


def read_lines_from_file(
    filepath: str, skip_comments: bool = False, encoding: str = "utf-8"
) -> list[str]:
    """
    Read lines from a text file.

    Args:
    filepath (str): The path to the text file.
    skip_comments (bool): Whether to skip lines starting with '#'. Default is False.
    encoding (str): The file encoding to apply - defaults to utf-8.

    Returns:
    list: A list of lines read from the file.
    """
    lines = []
    with open(filepath, encoding=encoding) as file:
        lines = [line.strip() for line in file]
    if skip_comments:
        lines = _remove_comments(lines)
    return lines


def read_text_from_file(filepath: str, encoding: str = "utf-8") -> str:
    """
    Read text from a text file.

    Args:
    filepath (str): The path to the text file.
    encoding (str): The file encoding to apply - defaults to utf-8.

    Returns:
    str: The text read from the file.
    """
    with open(filepath, encoding=encoding) as file:
        return file.read()


def _remove_comments(lines: list[str]) -> list[str]:
    """
    Remove lines starting with '#' from a list of lines.

    Args:
    lines (list): List of lines to filter.

    Returns:
    list: Filtered list of lines without comments.
    """
    filtered_lines = []
    for line in lines:
        if not line.startswith("#"):
            filtered_lines.append(line)
    return filtered_lines


def read_text_from_text_or_pdf_file_skipping_comments(filepath: str) -> str:
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


def write_text_lines_to_file(
    lines: list[str], filepath: str, encoding: str = "utf-8"
) -> None:
    """
    Write lines of text to a text file.

    Args:
    lines (list): List of lines to write to the file.
    filepath (str): The path to the output text file.
    encoding (str): The file encoding to apply - defaults to utf-8.
    """
    with open(filepath, encoding=encoding, mode="w") as file:
        for line in lines:
            file.write(line + util_text.LINE_END)


def write_array_to_file_skipping_empty(
    path_to_output_text_file: str, lines: list[str]
) -> None:
    """
    Write non-empty lines from an array to a file, skipping empty lines.

    Args:
    PATH_TO_OUTPUT_TEXT_FILE (str): The path to the output text file.
    lines (list): List of lines to write to the file.
    """
    with open(path_to_output_text_file, "w") as f:
        for line in lines:
            if line is not None and len(line) > 0:
                f.write(line + "\n")


def write_text_to_file(text: str, filepath: str, encoding: str = "utf-8") -> None:
    """
    Write text to a text file.

    Args:
    text (str): The text to write to the file.
    filepath (str): The path to the output text file.
    encoding (str): The file encoding to apply - defaults to utf-8.
    """
    with open(filepath, "w", encoding=encoding) as f:
        f.write(text)


def _get_last_part_of_path(file_path: str, sep: str) -> str:
    return file_path.split(sep)[-1]


def get_last_part_of_path(file_path: str) -> str:
    """
    Get the last part of a file path (filename).

    Args:
    file_path (str): The full file path.

    Returns:
    str: The last part of the file path (filename).
    """
    last_part = _get_last_part_of_path(file_path, os.sep)

    # Windows can sometimes use unix separators (e.g. from bash shell)
    if "/" in last_part:
        return _get_last_part_of_path(last_part, "/")
    return last_part
