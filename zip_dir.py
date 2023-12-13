import shutil
import sys

def print_usage():
    print(f"USAGE: {sys.argv[0]} <source directory> <path to new ZIP file>")

if len(sys.argv) != 3:
    print_usage()
    exit(42)

def create_zip(source_dir, output_zip_file):
    if output_zip_file.endswith(".zip"):
        output_zip_file = output_zip_file[:-4]
    shutil.make_archive(output_zip_file, 'zip', source_dir)

SOURCE_DIR = sys.argv[1]
OUTPUT_ZIP_FILE = sys.argv[2]

print(f"Zipping directory at {SOURCE_DIR} to {OUTPUT_ZIP_FILE} ...")
create_zip(SOURCE_DIR, OUTPUT_ZIP_FILE)
print("[done]")
