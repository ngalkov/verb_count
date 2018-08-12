"""Collect verb usage statistics through projects"""


import os
import argparse
from collections import Counter

from python_syntax_processing import extract_func_names, split_name_to_words
from natural_language_processing import filter_verbs


PROJECTS = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]


def parse_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dir",
        help="path to directory with projects",
        default="./",
        dest="projects_dir"
    )
    parser.add_argument(
        "--max_verbs",
        help="number of verbs to print",
        default=200
    )
    return parser.parse_args()


def find_verbs_in_file(python_file):
    verbs_list = []
    with open(python_file) as fp:
        file_content = fp.read()
    func_list = extract_func_names(file_content)
    for func_name in func_list:
        words_list = split_name_to_words(func_name)
        verbs_list += filter_verbs(words_list)
    return verbs_list


def find_python_files(project_dir):
    python_files = []
    for root, dirs, files in os.walk(project_dir, topdown=True):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files


def find_verbs_in_project(project_dir):
    verbs_list = []
    python_files = find_python_files(project_dir)
    for python_file in python_files:
        verbs_list += find_verbs_in_file(python_file)
    return verbs_list


def get_verbs_statistics(projects_dir="./"):
    verbs_statistics = Counter()
    verbs_count = 0
    for project in PROJECTS:
        project_dir = os.path.join(projects_dir, project)
        if not os.path.isdir(project_dir):
            continue
        project_verbs = find_verbs_in_project(project_dir)
        verbs_statistics.update(project_verbs)
        verbs_count += len(project_verbs)
    return verbs_statistics, verbs_count


def make_report(verbs_statistics, max_verbs, verbs_count):
    print('total %s verbs, %s unique' % (verbs_count, len(verbs_statistics)))
    for word, occurrence in verbs_statistics.most_common(max_verbs):
        print(word, occurrence)


if __name__ == "__main__":
    args = parse_cmd_line_args()
    verbs_statistics, verbs_count = get_verbs_statistics(args.projects_dir)
    make_report(verbs_statistics, args.max_verbs, verbs_count)
