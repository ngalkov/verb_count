import unittest
from python_syntax_processing import *


class TestSyntaxProcessing(unittest.TestCase):
    def test_build_syntax_tree(self):
        self.assertEqual(
            ast.dump(build_syntax_tree("a = 1")),
            "Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=1))])"
        )
        self.assertIsNone(build_syntax_tree("1 = 'bad syntax'"))

    def test_extract_func_names(self):
        with open("./syntax_tree_tests/func_name_extraction.py") as fp:
            code = fp.read()
        func_names = sorted(extract_func_names(code))
        self.assertListEqual(func_names, ["func1", "func2", "func3"])

    def test_split_name_to_words(self):
        cases = (
            ("", []),
            ("_", []),
            ("a", ["a"]),
            ("a_b", ["a", "b"]),
            ("___a___b_____cde__", ["a", "b", "cde"]),
            ("add_more_letters", ["add", "more", "letters"]),
        )
        for case in cases:
            self.assertListEqual(split_name_to_words(case[0]), case[1])


if __name__ == "__main__":
    unittest.main()
