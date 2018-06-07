import os
import argparse
import collections


def get_files_info(search_dir):
    files_info_dict = collections.defaultdict(list)
    for current_dir, full_dir, file_names in os.walk(search_dir):
        for file_name in file_names:
            full_path = os.path.join(current_dir, file_name)
            file_size = os.path.getsize(full_path)
            file_info = (file_name, file_size)
            files_info_dict[file_info].append(full_path)
    return files_info_dict


def print_duplicated_files(files_info_dict):
    for (file_name, size), paths in files_info_dict.items():
        if len(paths) > 1:
            print(file_name)
            for path in paths:
                print('--', path)
            print('\n')


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('search_dir', help='Path to search dir')
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    if os.path.isdir(args.search_dir):
        files_info_dict = get_files_info(args.search_dir)
        print_duplicated_files(files_info_dict)
    else:
        print('Specified path does not lead to the directory.')
