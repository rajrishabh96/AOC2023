import unittest
from main import *
class TestSumUpValues(unittest.TestCase):
    def test_inputs1(self):
        lines = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
            "pqw1sd2sad3asd"
        ]

        total_sum = calculate_total_of_digits(lines)

        # Assert that the total sum is equal to the expected value
        self.assertEqual(total_sum, 155)

    def test_inputs2(self):
        lines = [
            "abc",
        ]

        total_sum = calculate_total_of_digits(lines)

        # Assert that the total sum is equal to the expected value
        self.assertEqual(total_sum, 0)

if __name__ == '__main__':
    unittest.main()