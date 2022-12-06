import argparse
from modules.doc_generation import doc_generator
from modules.usable import *
from modules.data_cleaning import filter_data
import sys

def mk_docs(dict_args: dict):
    verify_folder_output()
    for obj in filter_data(dict_args['base_directory']):
        doc_generator(
            dict_args['template_directory'],
            obj, dict_args['file_name_pattern'],
            dict_args['flag']
        )

    if dict_args['flag'] == 1:
        clean_dir_md()

class Help(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        # Melhorar aqui o processo de printar o texto
        with open(file='src/cmd/about.txt', mode='rb') as f:
           data = f.read()
           print(data)
        parser.exit()

class About(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        print("about")
        parser.exit()

def main():
    parser = argparse.ArgumentParser(description='Documents auto-generated.')
    parser.add_argument('--about', nargs=0, help='About our project', action=Help)
    parser.add_argument('template_directory', help='Template dictionary.')
    parser.add_argument('base_directory', help='Database directory.')
    parser.add_argument('file_name_pattern', help='Output file pattern name.')
    args = parser.parse_args()

    if args['about']:
        with open('cmd/about.txt', 'rb') as file:
            print(file.text)
    else:
        mk_docs(dict(args._get_kwargs()))


if __name__ == '__main__':
    main()
