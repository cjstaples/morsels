import unittest
from winners import print_game_stats, games_won

NOT_VALID = 'Not a valid color'


def call_mytest_winners():
    # some people prefer sys.exit instead of break
    try:
        print_game_stats(5)
    except SystemExit:
        pass


class MyTestCase(unittest.TestCase):
    def test_num_one(self):
        # user only enter quit, program prints bye and breaks loop
        print_game_stats(5)
        actual = False
        expected = True
        assert actual == expected


    def test_num_two(self):
        # user enters blue = valid color so print it
        # then user enters quit so break out of loop = end program
        print_game_stats(5)
        actual = False
        expected = True
        assert actual == expected
