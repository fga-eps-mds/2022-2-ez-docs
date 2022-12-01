import argparse
from modules.doc_generation import doc_generator
from modules.usable import *
from modules.data_cleaning import filter_data


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
    parser = argparse.ArgumentParser(description='Documents auto-generated.')
    parser.add_argument('template_directory', help='Template dictionary.')
    parser.add_argument('base_directory', help='Database directory.')
    parser.add_argument('file_name_pattern', help='Output file pattern name.')
    parser.add_argument('--flag', help='Flag to output file extension. 0 for .md, 1 for .pdf', default=1)
    args = parser.parse_args()
    mk_docs(dict(args._get_kwargs()))


if __name__ == '__main__':
    main()
