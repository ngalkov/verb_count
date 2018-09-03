import unittest
from natural_language_processing import *


class TestNLP(unittest.TestCase):
    def test_is_verb(self):
        cases = (
            ("get", True),
            ("the", False),
            ("", False),
            (None, False)
        )
        for case in cases:
            self.assertEqual(is_verb(case[0]), case[1])

    def test_filter_verbs(self):
        self.assertEqual(
            filter_verbs(["get", "got", "gets", "the", "data", "", " "]),
            ["get", "got", "gets"]
        )


if __name__ == "__main__":
    unittest.main()
