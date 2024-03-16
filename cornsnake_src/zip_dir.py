import shutil

def create_zip(source_dir, output_zip_file):
    if output_zip_file.endswith(".zip"):
        output_zip_file = output_zip_file[:-4]
    shutil.make_archive(output_zip_file, 'zip', source_dir)
