from unittest import TestCase
from src.subdomains.date_handler import DateHandler

class TestDateTime(TestCase):
    def test_datetime_input_is_incorrect(self):            
        with self.assertRaises(Exception):
            DateHandler("2020-13-01 20:23")
        
        with self.assertRaises(Exception):
            DateHandler("2021/18/10 56:00")

        with self.assertRaises(Exception):
            DateHandler("1990-12-12 99:12")

        with self.assertRaises(Exception):
            DateHandler("2012-02-30 00:00")

        with self.assertRaises(Exception):
            DateHandler("2024/02/28 23:59")

        with self.assertRaises(Exception):
            DateHandler("2012-09-31 00:00")

    def test_datetime_input_is_correct(self):
        try:
            DateHandler("2020-12-01 20:23")
        except Exception:
            assert False
        
        try:
            DateHandler("2021-10-09 12:34")
        except Exception:
            assert False

        try:
            DateHandler("2024-02-28 23:59")
        except Exception:
            assert False

