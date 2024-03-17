"""
Functions for tracking progress and updating a progress bar.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_progress.html)
"""

import sys

from . import config

previous_percent = 0

def progress(count, total):
    """
    Function to update progress based on count and total.

    Args:
    count (int): The current count.
    total (int): The total count.

    Returns:
    None
    """
    global previous_percent

    percent = round(100.0 * count / float(total), 1)

    if config.MINIMIZE_PROGRESS_BAR_OUTPUT:
        if percent < previous_percent:
            # reset:
            previous_percent = percent
        else:
            if percent - previous_percent < 10:
                return
    previous_percent = percent

    _update_progress(percent)

def _update_progress(percent):
    """
    Function to update the progress bar based on percentage.

    Args:
    percent (float): The percentage of progress.

    Returns:
    None
    """
    bar_len = 60
    filled_len = int(round(bar_len * percent / float(100)))

    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    fmt = '[%s] %s%s ...' % (bar, percent, '%')
    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(fmt)
    sys.stdout.flush()

def complete():
    """
    Function to complete the progress bar by updating it to 100% and printing a new line.

    Returns:
    None
    """
    _update_progress(float(100))
    print("")  # ensure a new line
