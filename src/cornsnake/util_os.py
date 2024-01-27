import os
import platform

from . import util_log

logger = util_log.getLogger(__name__)

def is_windows():
    return os.name == 'nt'

def is_mac():
    return platform.system() == 'Darwin'

def is_unix():
    return not is_windows() and not is_mac()

if is_windows():
    import winreg

    def get_registry_key(top_key, reg_path, name):
        try:
            registry_key = winreg.OpenKey(top_key, reg_path, 0, winreg.KEY_READ)
            value, _regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    def is_windows_max_path_setting_on():
        path = r'SYSTEM\CurrentControlSet\Control\FileSystem'  # HKEY_LOCAL_MACHINE is implied
        key = 'LongPathsEnabled'
        value = get_registry_key(winreg.HKEY_LOCAL_MACHINE, path, key)
        if value is None:
            return False
        return str(value) == '1'

def log_os():
    logger.info("=== OS ===")
    logger.info(f"OS: {_os_platform()}")
    logger.info(f"DETAILS: {platform.system()} - {os.name} - {platform.release()}")

def _os_platform():
    if is_windows():
        return "Windows"
    if is_mac():
        return "Mac"
    if is_unix():
        return "Unix"
    return "(unknown)"
