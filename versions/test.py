import unittest
from versions import versions


class TestsVersions(unittest.TestCase):

    def testVersions(self):
        result = versions("1.2", "2.4")
        self.assertEqual(result, "2.4")

    def testNegativeVersions(self):
        result = versions("1.2", "-2.4")
        self.assertEqual(result, "1.2")

    def testDiferentSizeVersions(self):
        result = versions("1.2.4", "-2.4")
        self.assertEqual(result, "1.2.4")

    def testEquals(self):
        result = versions("1.2", "1.2")
        self.assertEqual(result, "Equals")

    def testDiferentSizeVersionsBig(self):
        result = versions("0.2.4.0.0.0.0.0.0.1.0", "2.4")
        self.assertEqual(result, "2.4")

    def testEquals(self):
        result = versions("1", "1")
        self.assertEqual(result, "Equals")

    def testBigNumbers(self):
        result = versions("1419.4","100.0")
        self.assertEqual(result, "1419.4")

    def testEquals(self):
        result = versions("0.0.01", "0.0.01")
        self.assertEqual(result, "Equals")
    
    def testInvalid(self):
        result = versions("0w.0.01", "0.0.01")
        self.assertEqual(result, 'Invalid Format')

    def testDiferentSizeVersions2(self):
        result = versions("0", "-1.0.01")
        self.assertEqual(result, "0")

if __name__ == '__main__':
    unittest.main()