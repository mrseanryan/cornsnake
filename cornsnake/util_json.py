"""
Functions for reading from and writing to a JSON file. The `read_from_json_file` function reads JSON data from a file, and the `write_to_json_file` function writes JSON data to a file.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_json.html)
"""

import json
import typing


def _json_to_string(value_json: typing.Any) -> str:
    return json.dumps(value_json, indent=0)


def are_same(settings1_json_str: str, settings2_json_str: str) -> bool:
    """Function to compare two JSON objects, ignoring differences in whitespace."""

    # parse and serialize to ignore any formatting differences:
    def _parse_and_serialize(json_str: str) -> str:
        value_json = json.loads(json_str)
        return _json_to_string(value_json)

    return _parse_and_serialize(settings1_json_str) == _parse_and_serialize(
        settings2_json_str
    )


def read_from_json_file(path_to_json: str, encoding: str = "utf-8") -> typing.Any:
    """
    Function to read JSON data from a file.

    Args:
    path_to_json (str): The path to the JSON file.
    encoding (str): The encoding of the file. Default is 'utf-8'.

    Returns:
    dict: The JSON data read from the file.
    """
    with open(path_to_json, encoding=encoding) as f:
        data = json.load(f)
        return data


def write_to_json_file(
    dict: dict,
    file_path: str,
    encoding: str = "utf-8",
    indent: int = 2,
    sort_keys: bool = False,
) -> None:
    """
    Function to write JSON data to a file.

    Args:
    dict (dict): The dictionary to be written to the file as JSON.
    file_path (str): The path to the output JSON file.
    encoding (str): The encoding of the file. Default is 'utf-8'.
    indent (int): The number of spaces to use for indentation. Default is 2.
    sort_keys (bool): Whether to sort the keys in the output JSON. Default is False.
    """
    json_object = json.dumps(dict, indent=indent, sort_keys=sort_keys)

    with open(file_path, "w", encoding=encoding) as outfile:
        outfile.write(json_object)


def sort_json_to_str(data: dict) -> str:
    """Function to return a JSON string with sorted keys.

    Args:
        data (dict): The dictionary to be converted to a JSON string.
    """
    return json.dumps(data, sort_keys=True)
