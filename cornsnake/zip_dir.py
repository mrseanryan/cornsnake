"""
Function for creating a zip archive from a directory. The `create_zip` function creates a zip archive of a specified directory.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/zip_dir.html)
"""
import shutil

def create_zip(source_dir, output_zip_file):
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
    shutil.make_archive(output_zip_file, 'zip', source_dir)
