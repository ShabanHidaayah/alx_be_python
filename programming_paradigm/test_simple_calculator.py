import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up a calculator instance for each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed signs
        self.assertEqual(self.calc.add(-5, 10), 5)
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
    
    def test_subtraction(self):
        """Test subtraction operation"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed signs
        self.assertEqual(self.calc.subtract(10, -5), 15)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
    
    def test_multiplication(self):
        """Test multiplication operation"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test mixed signs
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
    
    def test_division(self):
        """Test division operation"""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=7)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test negative division
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Test zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
