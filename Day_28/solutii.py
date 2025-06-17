# Day 28 - Solutions

import unittest

# Exercise 1:
def add(a, b):
    return a + b

# Exercise 3:
def is_palindrome(s):
    return s == s[::-1]

# Exercise 5:
def find_max(lst):
    return max(lst)

# Exercise 2, 4, 5:
class TestBasics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madonna"[::-1] == "madonna"))  # False
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 2]), 5)
        self.assertEqual(find_max([-10, -1]), -1)

if __name__ == '__main__':
    unittest.main()
