import unittest

from _bites._archive.summing import sum_numbers


class MyTestCase(unittest.TestCase):
    def test_sum_numbers_default_args(self):
        assert sum_numbers() == 5050
        assert sum_numbers(numbers=None) == 5050

    def test_sum_numbers_positive_inputs(self):
        assert sum_numbers(range(1, 11)) == 55
        assert sum_numbers([1, 2, 3]) == 6
        assert sum_numbers((1, 2, 3)) == 6

    def test_sum_numbers_negative_inputs(self):
        assert sum_numbers([]) == 0  # !! [] not the same as None


if __name__ == '__main__':
    unittest.main()
