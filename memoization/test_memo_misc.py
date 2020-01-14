import unittest

from memoization import memo_misc

class MiscTests(unittest.TestCase):

    """Tests for num_range"""

    def test_1x1(self):
        self.assertEqual(memo_misc.routes(1,1), 1)

    def test_3x3(self):
        self.assertEqual(memo_misc.routes(3,3), 6)

    def test_4x1(self):
        self.assertEqual(memo_misc.routes(4,1), 1)

    def test_4x2(self):
        self.assertEqual(memo_misc.routes(4,2), 4)

    def test_10x10(self):
        self.assertEqual(memo_misc.routes(10,10), 48620)
