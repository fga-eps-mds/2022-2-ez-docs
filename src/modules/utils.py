import os
import glob

def verify_pasta_output():
    path = 'output/'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:   
    # Create a new directory because it does not exist 
        os.makedirs(path)

def clean_dir_md():
    target_folder = 'output/'
    target_extension = 'md'

    target_filenames = glob.glob(target_folder + '*.' + target_extension)

    for filename in target_filenames:
     os.remove(filename)

    