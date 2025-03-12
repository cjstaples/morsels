import pytest

from perfect_squares import squares

def test_squares_2(key=2, value=4):
    actual = squares.perfect_squares_to_20()
    assert actual.get(key) == value


def test_squares_5(key=5, value=25):
    actual = squares.perfect_squares_to_20()
    assert actual.get(key) == value


def test_squares_8(key=8, value=64):
    actual = squares.perfect_squares_to_20()
    assert actual.get(key) == value


@pytest.mark.parametrize("key, value", [(16, 256), (3, 9), (19, 361), (21, None)])
def test_perfect_squares(key, value):
    actual = squares.perfect_squares_to_20()
    assert actual.get(key) == value


if __name__ == '__main__':
    import sys

    sys.exit()