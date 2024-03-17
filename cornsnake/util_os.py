"""
Functions for checking the operating system and logging OS information. The functions determine if the OS is Windows, Mac, or Unix, and log relevant OS details.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_os.html)
"""

import os
import platform

from . import util_log

logger = util_log.getLogger(__name__)

def is_windows():
    """
    Check if the current OS is Windows.

    Returns:
    bool: True if the OS is Windows, False otherwise.
    """
    return os.name == 'nt'

def is_mac():
    """
    Check if the current OS is Mac.

    Returns:
    bool: True if the OS is Mac, False otherwise.
    """
    return platform.system() == 'Darwin'

def is_unix():
    """
    Check if the current OS is Unix.

    Returns:
    bool: True if the OS is Unix, False otherwise.
    """
    return not is_windows() and not is_mac()

if is_windows():
    import winreg

    def get_registry_key(top_key, reg_path, name):
        """
        Get a value from Windows registry.

        Args:
        top_key: The top level key in the registry.
        reg_path: The path in the registry.
        name: The name of the registry key.

        Returns:
        str: The value of the registry key, or None if not found.
        """
        try:
            registry_key = winreg.OpenKey(top_key, reg_path, 0, winreg.KEY_READ)
            value, _regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    def is_windows_max_path_setting_on():
        """
        Check if the Windows max path setting is enabled.

        Returns:
        bool: True if the max path setting is enabled, False otherwise.
        """
        path = r'SYSTEM\CurrentControlSet\Control\FileSystem'  # HKEY_LOCAL_MACHINE is implied
        key = 'LongPathsEnabled'
        value = get_registry_key(winreg.HKEY_LOCAL_MACHINE, path, key)
        if value is None:
            return False
        return str(value) == '1'

def log_os():
    """
    Log OS information including platform, system, name, and release.
    """
    logger.info("=== OS ===")
    logger.info(f"OS: {_os_platform()}")
    logger.info(f"DETAILS: {platform.system()} - {os.name} - {platform.release()}")

def _os_platform():
    """
    Determine the platform of the OS.

    Returns:
    str: The platform of the OS (Windows, Mac, Unix, or unknown).
    """
    if is_windows():
        return "Windows"
    if is_mac():
        return "Mac"
    if is_unix():
        return "Unix"
    return "(unknown)"
