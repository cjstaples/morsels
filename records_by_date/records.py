import csv

from dateutil.parser import parse as parse_datetime


class RecordsByDate:
    def __init__(self, data):
        self.data = data

    @classmethod
    def read_csv(cls, path):
        data = {}
        with open(path) as handle:
            for row in csv.DictReader(handle):
                when = parse_datetime(row['date']).date()
                data[when] = row
        return cls(data)
