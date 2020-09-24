import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(100, 1), 101)
        self.assertEqual(calc.add(-88, 88), 0)
        self.assertEqual(calc.add(2, 2), 4)

if __name__ == '__main__':
    unittest.main()