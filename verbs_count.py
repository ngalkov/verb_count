"""Collect verb usage statistics through projects"""


import os
import argparse
from collections import Counter

from python_syntax_processing import extract_func_names, split_name_to_words
from natural_language_processing import filter_verbs


def parse_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dir",
        help="path to directory with projects",
        default="./",
    )
    parser.add_argument(
        "-p", "--projects",
        nargs='+',
        help="projects list to check",
        default=[]
    )
    parser.add_argument(
        "-l", "--projects_list",
        help="file with projects list to check"
    )
    parser.add_argument(
        "-m", "--max_verbs",
        help="number of verbs to print",
        type=int,
        default=200
    )
    parser.add_argument(
        "--no_magic",
        help="don't count verbs in magic methods",
        action="store_true",
        default=False
    )
    return parser.parse_args()


def read_file(file_path):
    """Return file content or None in case of error"""
    try:
        with open(file_path) as fp:
            return fp.read()
    except OSError:
        return None


def find_verbs_in_file(python_file, no_magic_methods=False):
    verbs_list = []
    file_content = read_file(python_file)
    func_list = extract_func_names(file_content)
    for func_name in func_list:
        if no_magic_methods and func_name.startswith("__") and func_name.endswith("__"):
            continue
        words_list = split_name_to_words(func_name)
        verbs_list.extend(filter_verbs(words_list))
    return verbs_list


def find_python_files(project_dir):
    python_files = []
    for root, dirs, files in os.walk(project_dir, topdown=True):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files


def find_verbs_in_project(project_dir, no_magic_methods=False):
    verbs_list = []
    python_files = find_python_files(project_dir)
    for python_file in python_files:
        verbs_list.extend(find_verbs_in_file(python_file, no_magic_methods=no_magic_methods))
    return verbs_list


def get_verbs_statistics(projects_list, no_magic_methods=False):
    verbs_statistics = Counter()
    verbs_count = 0
    for project in projects_list:
        if not os.path.isdir(project):
            continue
        project_verbs = find_verbs_in_project(project, no_magic_methods)
        verbs_statistics.update(project_verbs)
        verbs_count += len(project_verbs)
    return verbs_statistics, verbs_count


def make_report(verbs_statistics, max_verbs, verbs_count):
    print('total %s verbs, %s unique' % (verbs_count, len(verbs_statistics)))
    for word, occurrence in verbs_statistics.most_common(max_verbs):
        print(word, occurrence)


if __name__ == "__main__":
    args = parse_cmd_line_args()
    projects = args.projects
    if args.projects_list:
        with open(args.projects_list) as fp:
            projects.extend(map(str.strip, fp.readlines()))
    projects = [os.path.join(args.dir, project) for project in projects]
    verbs_statistics, verbs_count = get_verbs_statistics(projects, args.no_magic)
    make_report(verbs_statistics, args.max_verbs, verbs_count)
