import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)
        
    def test_first(self):
        self.assertEqual(fibonacci(1), 1)
        
    def test_positive_number(self):
        self.assertEqual(fibonacci(10), 55)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_invalid_type_text(self):
        with self.assertRaises(ValueError):
            fibonacci("text")

    def test_float_string(self):
        with self.assertRaises(ValueError):
            fibonacci("2.5")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            fibonacci("")

if __name__ == '__main__':
    unittest.main()