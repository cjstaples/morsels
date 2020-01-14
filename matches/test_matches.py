import unittest

from matches import matches_misc

class MiscTests(unittest.TestCase):

    """Tests for matches"""
    # testccdata = matches_misc.credit_card_data
    def setUp(self) -> None:
        pass

    def test_nothing(self):
        self.fail("shouldnt happen")

    def test_always_pass(self):
        self.assertEqual(1,1)
