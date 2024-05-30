import unittest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtract_numbers(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = multiply_numbers(4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == "__main__":
    unittest.main()
