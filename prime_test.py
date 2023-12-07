import unittest
# from devide import divide
from prime import is_prime2

class TestPrimeFile(unittest.TestCase):
    def test_negative_numbers_prime(self):
        self.assertFalse(is_prime2(-1))
        self.assertFalse(is_prime2(-10))

    def test_zero_and_one(self):
        self.assertFalse(is_prime2(0))
        self.assertFalse(is_prime2(1))

    def test_prime_numbers(self):
        self.assertTrue(is_prime2(2))
        self.assertTrue(is_prime2(3))
        self.assertTrue(is_prime2(5))
        self.assertTrue(is_prime2(7))
        self.assertTrue(is_prime2(11))
        self.assertTrue(is_prime2(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime2(4))
        self.assertFalse(is_prime2(6))
        self.assertFalse(is_prime2(8))
        self.assertFalse(is_prime2(9))
        self.assertFalse(is_prime2(10))

if __name__ == '__main__':
    unittest.main()