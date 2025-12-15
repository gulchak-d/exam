import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)
        
    def test_first(self):
        self.assertEqual(fibonacci(1), 1)
        
    def test_positive_number(self):
        # 10-й елемент Фібоначчі це 55
        self.assertEqual(fibonacci(10), 55)

    def test_negative_input(self):
        # Перевірка на генерацію виключення
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            fibonacci("text")

if __name__ == '__main__':
    unittest.main()