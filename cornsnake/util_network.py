"""
Download files or make a POST request without adding extra libraries.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_network.html)
"""

from datetime import datetime
import os
import urllib.request

from . import util_log

logger = util_log.getLogger(__name__)


def get_file(
    url: str,
    local_path_to_write_file: str,
    timeout: int = 60,
    headers: dict[str, str] = {},
) -> None:
    """
    Function to download a file from a URL to a local file path, via a HTTP GET request.

    Args:
    url (str): The URL to download from, via a GET request.
    timeout (int): Optional timeout for the request in seconds.
    """
    req = urllib.request.Request(
        url=url,
        data=None,
        headers=headers,
        origin_req_host=None,
        unverifiable=False,
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status == 200:
            with open(local_path_to_write_file, "wb") as file:
                file.write(response.read())
        else:
            raise RuntimeError(
                f"File download failed. HTTP status code: {response.status_code}"
            )


def _get_file_name_from_url(url: str, text_file_extensions: list[str]) -> str:
    # credit to scottleibrand

    # Strip any trailing /'s from the end of the URL
    stripped_url = url.rstrip("/")

    # Get the base name of the URL
    base_name = stripped_url.split("/")[-1]

    for ext in text_file_extensions:
        if base_name.endswith(ext):
            return base_name

    return base_name + ".html"


def _get_timestamped_filename(filename: str) -> str:
    # add timestamp to make unique filename, since URL content may have changed
    now = datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H%M%S")

    filename_parts = filename.split(".")
    extension = filename_parts[-1]
    filename_parts = filename_parts[:-1]
    filename_parts += [timestamp, extension]
    filename = ".".join(filename_parts)

    return filename


def get_file_timestamped(
    url: str,
    path_to_dir: str,
    prefix: str = "",
    text_file_extensions: list[str] = [".txt", ".html", ".md", ".yaml"],
    timeout: int = 60,
) -> str:
    """
    Function to download a *timestamped* file from a URL to an automatically generated local file path, via a HTTP GET request.
    This helps to ensure the latest copy of the URL is saved, in case there was a previous download.

    Args:
    url (str): The URL to download from, via a GET request.
    path_to_dir (str): The local directory to write the file to.
    prefix (str): Optional prefix for the new filename.
    text_file_extensions (list[str]): Optional file extensions to recognise - if the URL ending is not recognised, then the file is saved as '.html'.
    timeout (int): Optional timeout for the request in seconds.

    Returns:
    str: The path to the new local file.
    """
    filename = _get_file_name_from_url(url, text_file_extensions)

    filename = _get_timestamped_filename(filename)

    local_filepath = os.path.join(path_to_dir, f"{prefix}-{filename}")
    get_file(url, local_filepath, timeout)
    return local_filepath


def post_request(api_url: str, headers: dict[str, str], timeout: int = 60) -> bool:
    """
    Function to make a POST request to a specified API URL.

    Args:
    api_url (str): The URL to which the POST request will be made.
    headers (dict): The headers to be included in the request.
    timeout (int): The timeout for the request in seconds.

    Returns:
    bool: True if the POST request is successful (status code 200). Otherwise raises RuntimeError.
    """
    req = urllib.request.Request(
        url=api_url,
        data=None,
        headers=headers,
        origin_req_host=None,
        unverifiable=False,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status == 200:
            return True
        raise RuntimeError(f"POST failed. HTTP status code: [{response.status}]")
