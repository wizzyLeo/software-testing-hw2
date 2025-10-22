import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)  

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)  

    def test_divide_returns_quotient(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)  

    def test_divide_handles_non_even_results(self):
        calc = Calculator()
        result = calc.divide(7, 2)
        self.assertEqual(result, 3.5)  # Expect float result for non-even division

    def test_divide_by_zero_raises_error(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calc.divide(4, 0)  # Division by zero should not be allowed

if __name__ == "__main__":
    unittest.main()
