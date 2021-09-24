import unittest
from fmtcheck import *

class fmtchecktest(unittest.TestCase):
    # Тест
    def testCheckBinaryCorrect(self):
        data = [ "010110", "0b10101", "1", "0"]

        for s in data:
            self.assertTrue(CheckBinary(s), f'Input data: {s}')

    def testCheckBinaryIncorrect(self):

        data = [1123, None]

        for s in data:
            with self.assertRaises(TypeError):
                CheckBinary(s)

    def testCheckDate(self):
        data = ["15-65-1295", "87-56-4685", "54-78-5957", "99-99-0000"]
        # баг - принимает дни больше 31 и месяцы больше 12, год 0000
        for s in data:
            self.assertTrue(CheckDate(s), f'Input data: {s}')

    def testCheckDateIncorrect(self):

        data = [5949541, None]

        for s in data:
            with self.assertRaises(TypeError):
                CheckDate(s)

    def testCheckDecimal(self):
        data = ["-1651651.1651", "+8756,4685", "59.57", "651651."]

        for s in data:
            self.assertTrue(CheckDecimal(s), f'Input data: {s}')

    def testCheckDecimalIncorrect(self):
        data = [".1651", "65-465"]

        for s in data:
            self.assertFalse(CheckDecimal(s), f'Input data: {s}')

    def testCheckIPCorrect(self): #bug 255.255.255.255
        data = ["128.3.55.10", "0.0.0.0", "255.255.255.255"]

        for s in data:
            self.assertTrue(CheckIP(s), f'input data: {s}')

    def testCheckIPIncorrect(self):

        data = ["260.30.5.1", "a30.5.2.1"]

        for s in data:
            self.assertFalse(CheckIP(s), f'Input data: {s}')

    def testCheckHtmlColorCorrect(self):
        data = ["#ff00f4", "ff00f4", "004cbb"]

        for s in data:
            self.assertTrue(CheckHtmlColor(s), f'input data: {s}')

    def testCheckEmailCorrect(self):
        data = ["john.doe@example.com", "joh.n@doe.com"]

        for s in data:
            self.assertTrue(CheckEmail(s), f'input data: {s}')

    def testCheckEmailIncorrect(self):

        data = [1123, None]

        for s in data:
            with self.assertRaises(TypeError):
                CheckEmail(s)




if __name__ == "__main__":
    unittest.main()
