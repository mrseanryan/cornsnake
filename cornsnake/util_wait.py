"""
Function for waiting for a specified number of seconds. The `wait_seconds` function pauses the program execution for the specified number of seconds.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_wait.html)
"""

import time

def wait_seconds(seconds):
    """
    Function to pause program execution for a specified number of seconds.

    Args:
    seconds (int): The number of seconds to wait.

    Returns:
    None
    """
    print(f"    waiting {seconds}s...")
    time.sleep(seconds)
