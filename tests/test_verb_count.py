import unittest
from werbs_count import *


class TestFilesDetection(unittest.TestCase):
    def test_find_python_files(self):
        python_files = find_python_files("./files_detection/")
        self.assertListEqual(
            python_files,
            ["./files_detection/file1.py", "./files_detection/file2.py", "./files_detection/subdir\\file1.py"]
        )

    def test_find_verbs_in_project(self):
        self.assertListEqual(
            find_verbs_in_project("./projects/django"),
            ["make", "make", "do"]
        )

    def test_get_verbs_statistics(self):
        self.assertDictEqual(
            get_verbs_statistics("./projects"),
            {'make': 3, 'do': 2, 'get': 1}
        )
