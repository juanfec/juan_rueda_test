import unittest
from overlaps import overlaps


class TestsOverlaps(unittest.TestCase):

    def testIntervalOverlaps(self):
        result = overlaps((1, 3), (2, 4))
        self.assertEqual(result, True)

    def testIntervalNotOverlaps(self):
        result = overlaps((1, 2), (3, 4))
        self.assertEqual(result, False)

    def testNegativeIntervalNotOverlaps(self):
        result = overlaps((-2, -1), (-4, -3))
        self.assertEqual(result, False)

    def testSameInterval(self):
        result = overlaps((1, 1), (1, 1))
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()