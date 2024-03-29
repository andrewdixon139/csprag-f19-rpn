import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)

    def test_multiply(self): 
        result = rpn.calculate("12 8 *")
        self.assertEqual(96, result)

    def test_division_trunc(self): 
        result = rpn.calculate("12 8 /")
        self.assertEqual(1, result)

    def test_division(self): 
        result = rpn.calculate("24 8 /")
        self.assertEqual(3, result)

    def test_badinput(self): 
        with self.assertRaises(TypeError):
            rpn.calculate("1 2 3 +")
    
    def test_carat(self): 
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)
    
    def test_carat_zero(self): 
        result = rpn.calculate("5 0 ^")
        self.assertEqual(1, result)