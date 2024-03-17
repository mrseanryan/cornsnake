"""
Making a POST request using the urllib library.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_network.html)
"""

import urllib.request

from . import util_log

logger = util_log.getLogger(__name__)

def post_request(api_url, headers, timeout):
    """
    Function to make a POST request to a specified API URL.

    Args:
    api_url (str): The URL to which the POST request will be made.
    headers (dict): The headers to be included in the request.
    timeout (int): The timeout for the request in seconds.

    Returns:
    bool: True if the POST request is successful (status code 200), False otherwise.
    """
    req = urllib.request.Request(url=api_url, data=None, headers=headers, origin_req_host=None, unverifiable=False, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status == 200:
            return True
        print(f"POST failed [{response.status}]")
        return False
