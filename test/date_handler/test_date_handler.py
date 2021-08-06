from unittest import TestCase
from datetime import time
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
        
        with self.assertRaises(Exception):
            DateHandler("2012-09-31 99:00")
        
        with self.assertRaises(Exception):
            DateHandler("2012-09-31 34:99")
        
        with self.assertRaises(Exception):
            DateHandler("34:99")

        with self.assertRaises(Exception):
            DateHandler("14:99")

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
        
        try:
            DateHandler("23:59")
        except Exception:
            assert False

        try:
            DateHandler("22:19")
        except Exception:
            assert False

    def test_get_day_of_the_week(self):
        date1=DateHandler("2020-12-01 20:23")
        self.assertEqual(date1.get_day_as_integer(),1)

        date2=DateHandler("2021-10-09 20:23")
        self.assertEqual(date2.get_day_as_integer(),5)

        date3=DateHandler("2024-02-28 20:23")
        self.assertEqual(date3.get_day_as_integer(),2)

        date4=DateHandler("20:23")
        self.assertEqual(date4.get_day_as_integer(),-1)

        date5=DateHandler("00:23")
        self.assertEqual(date5.get_day_as_integer(),-1)

    def test_get_hour_as_time_object(self):
        date1=DateHandler("2020-12-01 20:23")
        self.assertEqual(date1.get_hour_as_time_object(),time(20,23))

        date2=DateHandler("2021-10-09 00:00")
        self.assertEqual(date2.get_hour_as_time_object(),time(0,0))

        date3=DateHandler("2024-02-28 09:35")
        self.assertEqual(date3.get_hour_as_time_object(),time(9,35))

