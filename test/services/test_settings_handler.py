from unittest import TestCase
from datetime import time
from src.services.settings_handler import SettingsHandler

class TestSettingHandler(TestCase):
    def test_day_key_as_integer_is_not_valid(self):            
        with self.assertRaises(Exception):
            SettingsHandler(-1)
        
        with self.assertRaises(Exception):
            SettingsHandler(-2)

        with self.assertRaises(Exception):
            SettingsHandler(-3)

        with self.assertRaises(Exception):
            SettingsHandler(7)

        with self.assertRaises(Exception):
            SettingsHandler(8)
        
        with self.assertRaises(Exception):
            SettingsHandler(9)

        with self.assertRaises(Exception):
            SettingsHandler("0")

        with self.assertRaises(Exception):
            SettingsHandler("0")

        with self.assertRaises(Exception):
            SettingsHandler("0")

        with self.assertRaises(Exception):
            SettingsHandler("0")
        
    def test_day_key_as_integer_is_valid(self):
        try:
            SettingsHandler(0)
        except Exception:
            assert False

        try:
            SettingsHandler(1)
        except Exception:
            assert False

        try:
            SettingsHandler(2)
        except Exception:
            assert False

        try:
            SettingsHandler(3)
        except Exception:
            assert False

        try:
            SettingsHandler(4)
        except Exception:
            assert False
        
        try:
            SettingsHandler(5)
        except Exception:
            assert False

        try:
            SettingsHandler(6)
        except Exception:
            assert False

    def test_restricted_time_segments(self):
        monday=SettingsHandler(0)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(monday.get_restricted_time_segments(),expected_time_segments)

        tuesday=SettingsHandler(1)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(tuesday.get_restricted_time_segments(),expected_time_segments)

        wednesday=SettingsHandler(2)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(wednesday.get_restricted_time_segments(),expected_time_segments)

    
    def test_restricted_plate_ending_digits(self):

        monday=SettingsHandler(0)
        expected_restricted_plate_ending_digits=[2,4,6,8,0]
        self.assertEqual(monday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        tuesday=SettingsHandler(1)
        expected_restricted_plate_ending_digits=[1,3,5,7,9]
        self.assertEqual(tuesday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        wednesday=SettingsHandler(2)
        expected_restricted_plate_ending_digits=[2,4,6,8,0]
        self.assertEqual(wednesday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        
      