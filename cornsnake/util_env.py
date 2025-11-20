"""
Utility functions for environment detection.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_env.html)
"""

from pathlib import Path
import sys


def is_in_docker() -> bool:
    """Check if the code is running inside a Docker container."""
    return Path("/.dockerenv").exists()


def is_in_a_test() -> bool:
    """Check if the code is running inside a test framework."""
    return "pytest" in sys.modules or "unittest" in sys.modules
