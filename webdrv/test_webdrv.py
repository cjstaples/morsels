import unittest
from webdrv.webdrv_sample import webdrv_logic


class WebdrvTestCase(unittest.TestCase):
    def test_webdrv_001(self):
        case = 1
        result = webdrv_logic(case)
        self.assertEqual(result, 1)

    def test_webdrv_002(self):
        case = 2
        result = webdrv_logic(case)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
