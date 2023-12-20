import os

TOTAL_BYTES_IN_GIGABYTE = 1000000000

def ensure_dir_exists(temp_git_fixer_dir):
    if not os.path.exists(temp_git_fixer_dir):
        os.makedirs(temp_git_fixer_dir)

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
