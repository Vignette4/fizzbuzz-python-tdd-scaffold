import unittest
from FizzBuzz import transform


class TestFizzBuzz(unittest.TestCase):
    def test_input_normal(self):
        self.assertEqual(transform(1), "1")

    def test_input_times_3(self):
        self.assertEqual(transform(3), "Fizz")

    def test_input_times_5(self):
        self.assertEqual(transform(5), "Buzz")

    def test_input_times_3_and_times_5(self):
        self.assertEqual(transform(15), "FizzBuzz")
