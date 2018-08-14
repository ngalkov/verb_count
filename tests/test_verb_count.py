import unittest
from verbs_count import *


class TestFilesDetection(unittest.TestCase):
    def test_find_python_files(self):
        python_files = find_python_files("./files_detection/")
        self.assertListEqual(
            python_files,
            ["./files_detection/file1.py", "./files_detection/file2.py", "./files_detection/subdir\\file1.py"]
        )

    def test_find_verbs_in_file(self):
        self.assertEqual(
            sorted(find_verbs_in_file("./projects/django/file1.py")),
            ["get", "make", "make"]
        )

    def test_find_verbs_in_project(self):
        self.assertListEqual(
            sorted(find_verbs_in_project("./projects/django")),
            ["do", "get", "make", "make"]
        )

    def test_get_verbs_statistics(self):
        verbs_statistics, verbs_count = get_verbs_statistics(
            ["./projects/django", "./projects/flask", "./projects/pyramid"])
        self.assertDictEqual(verbs_statistics, {"make": 4, "do": 2, "get": 2, "find": 1})
        self.assertEqual(verbs_count, 9)


if __name__ == "__main__":
    unittest.main()