"""
Functions for reading from and writing to a JSON file. The `read_from_json_file` function reads JSON data from a file, and the `write_to_json_file` function writes JSON data to a file.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_json.html)
"""
import json

def read_from_json_file(path_to_json, encoding='utf-8'):
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

def write_to_json_file(dict, file_path, encoding='utf-8', indent=2):
    """
    Function to write JSON data to a file.

    Args:
    dict (dict): The dictionary to be written to the file as JSON.
    file_path (str): The path to the output JSON file.
    encoding (str): The encoding of the file. Default is 'utf-8'.
    indent (int): The number of spaces to use for indentation. Default is 2.
    """
    json_object = json.dumps(dict, indent=indent)

    with open(file_path, "w", encoding=encoding) as outfile:
        outfile.write(json_object)
