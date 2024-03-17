"""
Functions for timing operations. The `start_timer` function starts a timer, `end_timer` ends the timer and calculates elapsed time, and `describe_elapsed_seconds` describes the elapsed time in seconds.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_time.html)
"""

from datetime import timedelta
import time

def start_timer():
    """
    Function to start a timer.

    Returns:
    float: The current time when the timer is started.
    """
    return time.time()

def end_timer(start):
    """
    Function to end the timer and calculate elapsed time.

    Args:
    start (float): The start time obtained from `start_timer` function.

    Returns:
    float: The number of seconds elapsed since the timer started.
    """
    end = time.time()
    seconds_elapsed = end - start
    return seconds_elapsed

def describe_elapsed_seconds(seconds_elapsed):
    """
    Function to describe the elapsed time in hours/minutes/seconds.

    Args:
    seconds_elapsed (float): The number of seconds elapsed.

    Returns:
    str: A formatted string representing the elapsed time in hours/minutes/seconds.
    """
    if seconds_elapsed is None:
        return "(unknown)"
    return f"{timedelta(seconds=round(seconds_elapsed))}s"
