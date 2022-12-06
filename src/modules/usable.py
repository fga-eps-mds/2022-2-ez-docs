import os
import glob
import argparse

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

class call_command_about(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        with open(file='cmd/about.txt') as f:
           data = f.read()
           print(data)
        parser.exit()

class call_command_architecture(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        with open(file='cmd/architecture.txt') as f:
           data = f.read()
           print(data)
        parser.exit()

class call_command_list(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        with open(file='cmd/list.txt') as f:
           data = f.read()
           print(data)
        parser.exit()

class call_command_help(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        with open(file='cmd/help.txt') as f:
           data = f.read()
           print(data)
        parser.exit()