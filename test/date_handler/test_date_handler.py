from unittest import TestCase
from src.subdomains.date_handler import DateHandler

class TestDateTime(TestCase):
    def test_datetime_input_is_incorrect(self):
        incorrect_dates=["2020-13-01 20:23", "2021/18/10 56:00", "1990-12-12 99:12","2012-02-29 00:00","2012-09-31 00:00","2024/02/28 23:59"]
        with self.assertRaises(Exception):
            for incorrect_date in incorrect_dates:
                DateHandler(incorrect_date)

    def test_datetime_input_is_correct(self):
        correct_dates=["2020-12-01 20:23", "2021-10-09 12:34", "2024-02-28 23:59"]
        for correct_date in correct_dates:
            try:
                DateHandler(correct_date)
            except Exception:
                assert False

