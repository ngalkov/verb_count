"""Collect verb usage statistics through projects"""


import os
from collections import Counter


PROJECTS = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]


def parse_cmd_line_args():
    raise NotImplementedError


def find_verbs_in_file(python_file):
    raise NotImplementedError


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
    for project in PROJECTS:
        project_dir = os.path.join(projects_dir, project)
        if not os.path.isdir(project_dir):
            continue
        project_verbs = find_verbs_in_project(project_dir)
        verbs_statistics.update(project_verbs)
    return verbs_statistics


def make_report(verbs_statistics, max_verbs):
    raise NotImplementedError


if __name__ == "__main__":
    args = parse_cmd_line_args()
    verbs_statistics = get_verbs_statistics(args.projects_dir)
    make_report(verbs_statistics, args.max_verbs)
