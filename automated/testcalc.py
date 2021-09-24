import unittest
from calc import *
#можно по другому  -  import calc

class CalcTest(unittest.TestCase):
    def testAdd(self):
        result = Add(1,3)
        self.assertEqual(result, 4)

    def testSub(self):
        self.assertEqual(Sub(5,2), 3)
        self.assertEqual(Sub(1,-1), 0)

if __name__ == '__main__':
    unittest.main()
