import argparse
from mkdocs_s7.modules.doc_generation import doc_generator
from mkdocs_s7.modules.usable import *
from mkdocs_s7.modules.data_cleaning import filter_data

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

def main():
    parser = argparse.ArgumentParser(description='Documents auto-generated.', add_help=False)
    parser.add_argument('--about', nargs=0, help='About our project', action=call_command)
    parser.add_argument('--architecture', nargs=0, help='Architecture stuff', action=call_command)
    parser.add_argument('--help', nargs=0, help='How to use it', action=call_command)
    parser.add_argument('--list', nargs=0, help='Command list', action=call_command)
    parser.add_argument('template_directory', help='Template dictionary.')
    parser.add_argument('base_directory', help='Database directory.')
    parser.add_argument('file_name_pattern', help='Output file pattern name.')
    args = parser.parse_args()
    mk_docs(dict(args._get_kwargs()))


if __name__ == '__main__':
    main()
