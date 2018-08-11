import unittest
from werbs_count import *


class TestFilesDetection(unittest.TestCase):
    def test_find_python_files(self):
        python_files = find_python_files("./files_detection/")
        self.assertListEqual(
            python_files,
            ["./files_detection/file1.py", "./files_detection/file2.py", "./files_detection/subdir\\file1.py"]
        )

