import unittest
from records import RecordsByDate
from datetime import date


class TestRecordsByDate(unittest.TestCase):
    def test_load_csv(self):
        recs = RecordsByDate.read_csv('testdata.csv')
        actual = recs.data[date(2034, 11, 30)]
        expected = {
            'date': '2034-11-30',
            'email': 'alpha@powerfulpython.com',
            'status': 'active',
            'source': 'facebook',
            }
        self.assertEqual(expected, actual)
