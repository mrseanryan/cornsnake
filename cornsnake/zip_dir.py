"""
Functions for creating a zip archive from a directory or a list of files.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/zip_dir.html)
"""

import shutil
import zipfile


def create_zip(source_dir: str, output_zip_file: str) -> None:
    """
    Function to create a zip archive from a directory.

    Args:
    source_dir (str): The path to the source directory to be zipped.
    output_zip_file (str): The name of the output zip file.

    Returns:
    None
    """
    if output_zip_file.endswith(".zip"):
        output_zip_file = output_zip_file[:-4]
    shutil.make_archive(output_zip_file, "zip", source_dir)


def create_zip_of_files(
    files_to_include: list[str], root_dir: str, path_to_output_zipfile: str
) -> list[str]:
    """
    Function to create a zip archive from a list of files.

    Args:
    files_to_include (list[str]): List of filepaths to include.
    root_dir (str): The root dir to use when deciding the relative path inside the ZIP.
    path_to_output_zipfile (str): The path to the output zip file.

    Returns:
    list[str]: List of file paths inside the ZIP.
    """
    if not files_to_include:
        return []
    with zipfile.ZipFile(path_to_output_zipfile, "w") as zip:
        file_names = []
        for file_name in files_to_include:
            short_file_name = file_name.replace(root_dir, "")
            file_names.append(short_file_name)
            zip.write(file_name, short_file_name)
        return file_names
