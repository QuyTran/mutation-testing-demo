import unittest
from devide import divide
# from prime import is_prime2

class TestDevideFile(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(9.0, 2), 4.5)

    def test_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_by_one(self):
        self.assertEqual(divide(10, 1), 10)
        self.assertEqual(divide(-10, 1), -10)

    def test_zero_divided_by_number(self):
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(0, -1), 0)

if __name__ == '__main__':
    unittest.main()