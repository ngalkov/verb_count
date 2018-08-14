This is an educational project

---
# Verb counter
Command line tool that collects verb usage statistics in function names for python projects.

## DESCRIPTION
Script scans python projects, looks for function names in python files, counts verb usage in such names and prints the most frequently used verbs and their quantity.  
Verbs in magic methods (like `__get__`, `__set__`) can be excluded from counting (see USAGE below). 

## USAGE
`verbs_count.py [-h] [-d DIR] [-p PROJECTS [PROJECTS ...]] [-l PROJECTS_LIST] [-m MAX_VERBS] [--no_magic]`  

Command line arguments are:
```
-h, --help            show this help message and exit
-d DIR, --dir DIR     path to directory with projects
-p PROJECTS [PROJECTS ...], --projects PROJECTS [PROJECTS ...]
                      projects list to check
-l PROJECTS_LIST, --projects_list PROJECTS_LIST
                      file with projects list to check
-m MAX_VERBS, --max_verbs MAX_VERBS
                      number of verbs to print
--no_magic            don't count verbs in magic methods
```

## Requirements
Python 3.6 or higher  
Python packages according to requirements.txt

## Tests
A test suite is provided with complete environment (`./tests` folder).  
