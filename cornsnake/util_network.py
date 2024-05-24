"""
Download files or make a POST request without adding extra libraries.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_network.html)
"""

import requests
import urllib.request

from . import util_log

logger = util_log.getLogger(__name__)

def get_file(url, local_path_to_write_file, timeout=60):
    """
    Function to download a file from a URL to a local file path, via a HTTP GET request.

    Args:
    url (str): The URL to download from, via a GET request.
    timeout (int): The timeout for the request in seconds.
    """
    response = requests.get(url, timeout=timeout)
    if response.status_code == 200:
        with open(local_path_to_write_file, "wb") as file:
            file.write(response.content)
    else:
        raise RuntimeError(f"File download failed. HTTP status code: {response.status_code}")

def post_request(api_url, headers, timeout=60):
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
