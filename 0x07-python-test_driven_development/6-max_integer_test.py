#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('16-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_assert_true(self):
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)
        self.assertTrue(max_integer([1, 3, 4, 2]), 4)

    def test_list_None(self):
        self.assertEqual(max_integer([]), None)

    def test_not_None(self):
        self.assertIsNotNone(max_integer([1, 2, 3, 4]))
        self.assertIsNotNone(max_integer([1, 3, 4, 2]))

    def test_strings_list(self):
        self.assertEqual(max_integer(["1", "2", "3", "4"]), "4")
        self.assertEqual(max_integer(["1", "3", "4", "2"]), "4")

    def test_letters_strings_list(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer(["e", "z", "q", "r"]), "z")

    def test_floats_list(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([1.0, 3.0, 4.0, 2.0]), 4.0)

    def test_big_values_list(self):
        self.assertEqual(max_integer([110, 200, 350, 4230]), 4230)
        self.assertEqual(max_integer([10100, 30000, 401203]), 401203)

    def test_neg_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_list(self):
        self.assertEqual(max_integer(["-1", "1", "c", "m"]), "m")


if __name__ == "__main__":
    unittest.main()
