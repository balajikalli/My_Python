import unittest

def divide_numbers(a, b):
    try:
        result = a / b
        return result  # Return the result for testing purposes
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except TypeError:
        raise TypeError("Both arguments must be numbers.")

class TestDivisionFunction(unittest.TestCase):
    
    def test_divide_by_zero(self):
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)

    def test_divide_by_non_number(self):
        # Test division by a non-number
        with self.assertRaises(TypeError):
            divide_numbers(10, "a")

    def test_valid_division(self):
        # Test valid division
        self.assertEqual(divide_numbers(10, 2), 5.0)

if __name__ == '__main__':
    unittest.main()