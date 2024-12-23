"""
Functions for checking and validating configuration settings in the config.py file.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_validate.html)
"""

import os
import re
import typing

from . import config
from . import util_date


def _check_is_boolean(value: typing.Any, name: str) -> str | None:
    """
    Check if a value is a boolean.

    Args:
    value (bool): The value to check.
    name (str): The name of the value.

    Returns:
    str: An error message if value is not a boolean, None otherwise.
    """
    if not isinstance(value, bool):
        return f"{name} must be a boolean (True or False)"

    return None


def _check_is_string_or_empty(value: typing.Any, name: str) -> str | None:
    """
    Check if a value is a string and not empty.

    Args:
    value (str): The value to check.
    name (str): The name of the value.

    Returns:
    str: An error message if value is not a string or empty, None otherwise.
    """
    if not isinstance(value, str):
        return f"{name} must be a string"
    if len(value.strip()) != len(value):
        return f"{name} must not have leading or trailing whitespace"

    return None


def _check_is_string_not_empty(value: typing.Any, name: str) -> str | None:
    """Check if a value is a string and not empty.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a string or empty, None otherwise."""
    error = _check_is_string_or_empty(value, name)
    if error:
        return error
    if len(value.strip()) == 0:
        return f"{name} must not be empty"
    return None


def _check_is_list_of_strings_or_empty(value: typing.Any, name: str) -> str | None:
    """Check if a value is a list of strings or empty.
    Args:
    value (list): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a list or contains non-string elements, None otherwise.
    """
    if not isinstance(value, list):
        return f"{name} must be a list!"
    for val in value:
        error = _check_is_string_not_empty(val, f"Value in {name}")
        if error:
            return error
    return None


def _check_is_path_to_file_or_directory(value: typing.Any, name: str) -> str | None:
    """Check if a value is a path to an existing file or directory.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid path, None otherwise."""
    error = _check_is_string_not_empty(value, name)
    if error:
        return error
    if not os.path.exists(value):
        return f"The value of {name} must be a path to an existing file"
    return None


def _check_is_path_to_file(value: typing.Any, name: str) -> str | None:
    """Check if a value is a path to an existing file.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid file path, None otherwise."""
    error = _check_is_path_to_file_or_directory(value, name)
    if error:
        return error
    if not os.path.isfile(value):
        return f"The value of {name} must be a path to a file (not a directory)"
    return None


def _check_is_path_to_dir(value: typing.Any, name: str) -> str | None:
    """Check if a value is a path to an existing directory.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid directory path, None otherwise."""
    error = _check_is_path_to_file_or_directory(value, name)
    if error:
        return error
    if not os.path.isdir(value):
        return f"The value of {name} must be a path to a directory (not a file)"
    return None


def _check_is_path_to_dir_or_empty(value: str | None, name: str) -> str | None:
    """Check if a value is a path to an existing directory or empty.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid directory path or empty, None otherwise.
    """
    if value is None or len(value) == 0:
        return None
    return _check_is_path_to_dir(value, name)


def _check_is_date_or_none(value: str | None, name: str) -> str | None:
    """Check if a value is a date or empty.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid date or empty, None otherwise."""
    if value is None or len(value) == 0:
        return None
    error_message = f"{name} must be a date in format 'yy-mm-dd'"
    try:
        date_value = util_date.parse_yyyy_mm_dd(value)
        if not date_value:
            return error_message
    except Exception:
        return error_message
    return None


def is_valid_blob_size(value: str) -> bool:
    """Check if a value is a valid blob size.
    Args:
    value (str): The value to check.
    Returns:
    bool: True if the value is a valid blob size, False otherwise."""
    if not value or len(value) == 0:
        return False
    pat = re.compile(r"[0-9]+[KMG]+")
    return True if re.fullmatch(pat, value) else False


def _check_is_blob_size(value: str, name: str) -> str | None:
    """Check if a value is a string and a valid blob size.
    Args:
    value (str): The value to check.
    name (str): The name of the value.
    Returns:
    str: An error message if value is not a valid blob size, None otherwise."""
    """Example of how to check configuration"""
    error = _check_is_string_not_empty(value, name)
    if error:
        return error
    if not is_valid_blob_size(value):
        return f"{name} must be like 256K or 1M or 1G"
    return None


# Example of how to check configuration
def _get_config_error() -> str | None:
    """Validate settings in config.py
    Returns:
    str: An error message if any configuration value is invalid, None otherwise."""
    """Validate settings in config.py"""
    # required
    error = _check_is_boolean(config.IS_VERBOSE, "IS_VERBOSE")
    if error is not None:
        return error

    error = _check_is_path_to_file(config.PATH_TO_GIT, "PATH_TO_GIT")
    if error is not None:
        return error

    # optional
    error = _check_is_date_or_none(config.date_param, "date_param")
    if error is not None:
        return error

    error = _check_is_path_to_dir_or_empty(config.path_to_repo_dir, "path_to_repo_dir")
    if error is not None:
        return error

    error = _check_is_list_of_strings_or_empty(config.branches, "branches")
    if error is not None:
        return error

    error = _check_is_string_or_empty(config.file_extensions, "file_extensions")
    if error is not None:
        return error

    error = _check_is_blob_size(config.blob_size, "blob_size")
    if error is not None:
        return error

    return None


# Validate settings in config.py
def validate() -> None:
    """Validate settings in config.py
    Raises:
    SystemExit: If any configuration value is invalid, with an error message.
    """
    """Validate settings in config.py"""
    error = _get_config_error()
    if error is not None:
        raise SystemExit(
            f"CONFIG ERROR: {error}. Please check the settings in config.py"
        )


def check_is_branch_name_or_empty(
    value: typing.Any, name: str = "branch name"
) -> str | None:
    """
    Check the given text is not empty and does not have a prefix like 'origin/'.
    """
    error = _check_is_string_or_empty(value, name)
    if error:
        return error
    if len(value) == 0:
        return None
    if "/" in value:
        return f"{name} must be a branch name, without any prefix like origin/"
    return None
