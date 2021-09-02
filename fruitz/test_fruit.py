import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def writeit(name):
    print(" " + name)


def test_basket():
    writeit("test for fruit basket")
    assert fruit_basket


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    writeit("test for fruit in basket")
    assert my_fruit in fruit_basket
