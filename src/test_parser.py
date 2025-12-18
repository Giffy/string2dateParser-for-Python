import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from parser import parse_date
import datetime as dt
import exceptions

class TestParser(unittest.TestCase):

    def test_parse_date_with_format(self):
        self.assertEqual(parse_date("2025-01-15", "%Y-%m-%d"), dt.datetime(2025, 1, 15))
        self.assertEqual(parse_date("2025/01/15", "%Y/%m/%d"), dt.datetime(2025, 1, 15))
        self.assertEqual(parse_date("2025/01/15T08:56:18", "%Y/%m/%dT%H:%M:%S"), dt.datetime(2025, 1, 15, 8, 56, 18))
        self.assertEqual(parse_date("2025/01/15T08:56:18z", "%Y/%m/%dT%H:%M:%Sz"), dt.datetime(2025, 1, 15, 8, 56, 18))
        self.assertEqual(parse_date("2025-01-15 8:56 AM", "%Y-%m-%d %I:%M %p"), dt.datetime(2025, 1, 15, 8, 56))
        self.assertEqual(parse_date("2025-01-15 8:56 PM", "%Y-%m-%d %I:%M %p"), dt.datetime(2025, 1, 15, 20, 56))
        self.assertEqual(parse_date("2025-01-15 8:56:18", "%Y-%m-%d %I:%M:%S"), dt.datetime(2025, 1, 15, 8, 56, 18))
        self.assertEqual(parse_date("2025-01-15T08:56:18.000000+01:00", "%Y-%m-%dT%H:%M:%S.%f%z"), dt.datetime(2025, 1, 15, 8, 56, 18, tzinfo=dt.timezone(dt.timedelta(seconds=3600))))
        self.assertEqual(parse_date("2025-01-15T08:56:18.000+01:00", "%Y-%m-%dT%H:%M:%S.%f%z"), dt.datetime(2025, 1, 15, 8, 56, 18, tzinfo=dt.timezone(dt.timedelta(seconds=3600))))

    def test_parse_date_with_format_error(self):
        self.assertRaises(exceptions.InvalidDateFormatError, parse_date, "2025-01+15", "%Y-%m-%d")

    def test_parse_date_timestamp(self):
        self.assertEqual(parse_date("1736927778", timestamp="s"), dt.datetime(2025, 1, 15, 8, 56, 18))
        self.assertEqual(parse_date("1736927778000", timestamp="m"), dt.datetime(2025, 1, 15, 8, 56, 18, 000))
        self.assertEqual(parse_date("1736927778000100", timestamp="n"), dt.datetime(2025, 1, 15, 8, 56, 18, 100))

    # def test_parse_date_iso_format(self):
    #     self.assertEqual(parse_date("2025-01-15"), dt.datetime(2023, 4, 1))
    #     self.assertEqual(parse_date("2025/01/15"), dt.datetime(2000, 2, 29))

    # def test_parse_date_iso_format_error(self):
    #     self.assertRaises(ValueError, parse_date("2025-13-15", "%Y-%m-%d"))
    #     self.assertEqual(parse_date("2023/12/41"), None)

    # def test_parse_date_hour(self):
    #     self.assertEqual(parse_date("2023-04-01 12:22:22"), dt.datetime(2023, 4, 1, 12, 22, 22))
    #     self.assertEqual(parse_date("2000/02/29 12:22:22"), dt.datetime(2000, 2, 29, 12, 22, 22))


if __name__ == '__main__':
    unittest.main()
