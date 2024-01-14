import os
import shutil

TOTAL_BYTES_IN_GIGABYTE = 1000000000

def copy_directory(from_path, to_path):
    shutil.copytree(from_path, to_path)

def ensure_dir_exists(temp_git_fixer_dir):
    if not os.path.exists(temp_git_fixer_dir):
        os.makedirs(temp_git_fixer_dir)

def find_files_by_extension(dir_path, extension):
    found_files = []
    contents = os.listdir(dir_path)
    for content in contents:
        path_to_sub = os.path.join(dir_path, content)
        if os.path.isfile(path_to_sub) and path_to_sub.endswith(extension):
            found_files.append(path_to_sub)
    return found_files

def get_directory_of_this_script():
    return os.path.dirname(os.path.realpath(__file__))

def get_total_dir_size_in_bytes(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def get_total_dir_size_in_gigabytes(start_path):
    return get_total_dir_size_in_bytes(start_path) / TOTAL_BYTES_IN_GIGABYTE

def is_empty_directory(path_to_file):
    if os.path.isfile(path_to_file):
        return False
    contents = os.listdir(path_to_file)
    return len(contents) == 0

def write_text_to_file(text, filepath):
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(text)
