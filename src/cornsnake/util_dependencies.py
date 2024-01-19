import os
import sys

from . import util_git
from . import util_print

PY_MAJOR = 3
PY_MIN_MINOR = 12

GIT_MAJOR = 2
GIT_MIN_MINOR = 42

def _raise_versions_error(program, message):
    raise SystemExit(f"DEPENDENCIES ERROR: {message}. Please check your version of {program}")

def _check_major_versions_equal(program, actual, expected):
    if actual != expected:
        _raise_versions_error(program, f"{program} major version must be {expected} - but you are using {actual}")

def _check_minor_version_greater_than_or_equal(program, actual, expected_major, expected_minor):
    if actual < expected_minor:
        _raise_versions_error(program, f"{program} version must be at least {expected_major}.{expected_minor} - but you are using {expected_major}.{actual}")

def _dump_current_version(program, version):
    util_print.print_custom_with_logger(f"Using {program} version {version}", logger)

def check_python_version():
    version = sys.version_info
    program = "Python"
    _dump_current_version(program, str(version))
    _check_major_versions_equal(program, version.major, PY_MAJOR)
    _check_minor_version_greater_than_or_equal(program, version.minor, PY_MAJOR, PY_MIN_MINOR)

def check_git_version():
    # example: 'git version 2.42.0.windows.1'
    result_parts = util_git.execute_command('--version', [], os.getcwd()).split(" ")
    version = result_parts[-1]
    version_parts = version.split(".")
    actual_major = int(version_parts[0])
    actual_minor = int(version_parts[1])
    program = "git"
    _dump_current_version(program, version)
    _check_major_versions_equal(program, actual_major, GIT_MAJOR)
    _check_minor_version_greater_than_or_equal(program, actual_minor, GIT_MAJOR, GIT_MIN_MINOR)
