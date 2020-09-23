import unittest
from webdrv.webdrv_sample import webdrv_logic


class FizzBuzzTestCase(unittest.TestCase):
    def test_fizzbuzz_001(self):
        case = 1
        result = webdrv_logic(case)
        self.assertEqual(result, 1)

    def test_fizzbuzz_003(self):
        case = 3
        result = webdrv_logic(case)
        self.assertEqual(result, 'Fizz')

    def test_fizzbuzz_005(self):
        case = 5
        result = webdrv_logic(case)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz_015(self):
        case = 15
        result = webdrv_logic(case)
        self.assertEqual(result, 'FizzBuzz')

    def test_fizzbuzz_098(self):
        case = 98
        result = webdrv_logic(case)
        self.assertEqual(result, 98)

    def test_fizzbuzz_099(self):
        case = 99
        result = webdrv_logic(case)
        self.assertEqual(result, 'Fizz')

    def test_fizzbuzz_100(self):
        case = 100
        result = webdrv_logic(case)
        self.assertEqual(result, 'Buzz')


if __name__ == '__main__':
    unittest.main()
