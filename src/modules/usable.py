import os
import glob


def verify_folder_output():
    # Check whether the specified path exists or not
    path = 'output/'
    exist = os.path.exists(path)
    if not exist:
        # Create a new directory because it does not exist
        os.makedirs(path)


def clean_dir_md():
    target_folder = 'output/'
    target_extension = 'md'
    # Find all the pathnames matching with the specified (target), according to the rules used by the Unix.
    target_file_names = glob.glob(target_folder + '*.' + target_extension)
    # Delete the files.
    for file_name in target_file_names:
        os.remove(file_name)
