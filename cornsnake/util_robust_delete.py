"""
Functions for recursively deleting directories and their contents.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_robust_delete.html)
"""

import os
import shutil
import stat

def _rmrf(temp_dir):
    """
    Recursively delete a directory and its contents.

    - Give this user read, write, execute permissions (so we can navigate and delete) but without affecting other users.

    Args:
    temp_dir (str): The path to the directory to be deleted.
    """
    st = os.stat(temp_dir)
    os.chmod(temp_dir, st.st_mode | stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)
    shutil.rmtree(temp_dir)

def _delete_files_recursively(temp_dir):
    """
    Recursively delete files in a directory.

    Args:
    temp_dir (str): The path to the directory containing files to be deleted.
    """
    for dirpath, _dirnames, filenames in os.walk(temp_dir):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                os.remove(fp)
            except FileNotFoundError:
                pass  # Intentionally NOT passing exception onwards
            except PermissionError:
                pass  # Intentionally NOT passing exception onwards

def _delete_dirs_recursively(temp_dir):
    """
    Recursively delete directories in a directory.

    Args:
    temp_dir (str): The path to the directory containing directories to be deleted.
    """
    for dirpath, dirnames, _filenames in os.walk(temp_dir):
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            try:
                _rmrf(dp)
            except FileNotFoundError:
                pass  # Intentionally NOT passing exception onwards
            except PermissionError:
                pass  # Intentionally NOT passing exception onwards

def _delete_dir_contents(temp_dir):
    """
    Delete files and directories in a directory.

    Args:
    temp_dir (str): The path to the directory containing files and directories to be deleted.
    """
    _delete_files_recursively(temp_dir)
    _delete_dirs_recursively(temp_dir)

def delete_dirs(temp_dirs_to_delete):
    """
    Delete directories and their contents.
    - Python holds on to some paths - so delete as much as we can

    Args:
    temp_dirs_to_delete (list): A list of directory paths to be deleted.
    """
    dirs_with_locked_items = []
    # faster delete:
    for temp_dir in temp_dirs_to_delete:
        try:
            _rmrf(temp_dir)
        except FileNotFoundError:
            dirs_with_locked_items.append(temp_dir)
            # Intentionally NOT passing exception onwards
        except PermissionError:
            dirs_with_locked_items.append(temp_dir)
            # Intentionally NOT passing exception onwards

    # slower, more robust delete:
    for temp_dir in dirs_with_locked_items:
        _delete_dir_contents(temp_dir)
