from unittest import TestCase
from datetime import time
from src.services.time_methods import is_time_in_range

class TestTimeMethods(TestCase):
    def test_is_time_in_range(self):
        #Array elements go in this order: start time, end time, trial time
        times=[time(7,0),time(10,30),time(8,30)]
        self.assertTrue(is_time_in_range(*times))

        #Array elements go in this order: start time, end time, trial time
        times=[time(14,23),time(14,23),time(14,23)]
        self.assertTrue(is_time_in_range(*times))

        # #Array elements go in this order: start time, end time, trial time
        times=[time(0,0),time(1,30),time(0,30)]
        self.assertTrue(is_time_in_range(*times))

        # #Array elements go in this order: start time, end time, trial time
        times=[time(0,0),time(0,0),time(0,0)]
        self.assertTrue(is_time_in_range(*times))

        # #Array elements go in this order: start time, end time, trial time
        times=[time(8,35),time(10,0),time(8,35)]
        self.assertTrue(is_time_in_range(*times))

         # #Array elements go in this order: start time, end time, trial time
        times=[time(8,35),time(12,49),time(12,49)]
        self.assertTrue(is_time_in_range(*times))

    def test_is_not_time_in_range(self):
        #Array elements go in this order: start time, end time, trial time
        times=[time(7,0),time(10,30),time(10,31)]
        self.assertFalse(is_time_in_range(*times))

        #Array elements go in this order: start time, end time, trial time
        times=[time(14,23),time(14,23),time(14,24)]
        self.assertFalse(is_time_in_range(*times))

        #Array elements go in this order: start time, end time, trial time
        times=[time(0,0),time(1,30),time(2,30)]
        self.assertFalse(is_time_in_range(*times))

        #Array elements go in this order: start time, end time, trial time
        times=[time(0,0),time(0,0),time(0,1)]
        self.assertFalse(is_time_in_range(*times))

