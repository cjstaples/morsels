import unittest
from winners import print_game_stats, games_won

NOT_VALID = 'Not a valid color'


class MyTestCase(unittest.TestCase):

    def test_print_game_stats(capfd):
        winner_prints = ["sara has won 0 games",
                         "bob has won 1 game",
                         "tim has won 5 games",
                         "julian has won 3 games",
                         "jim has won 1 game"]

        print_game_stats(games_won)
        output = capfd.readouterr()[0].splitlines()

        # dict + Python 3.7 = insert order should be retained
        for line in winner_prints:
            assert line in output
