from unittest import TestCase
from datetime import time
from src.services.settings_handler import SettingsHandler

mode="testing"
class TestSettingHandler(TestCase):
    def test_day_key_as_integer_is_not_valid(self):            
        with self.assertRaises(Exception):
            SettingsHandler(-1,mode)
        
        with self.assertRaises(Exception):
            SettingsHandler(-2,mode)

        with self.assertRaises(Exception):
            SettingsHandler(-3,mode)

        with self.assertRaises(Exception):
            SettingsHandler(7,mode)

        with self.assertRaises(Exception):
            SettingsHandler(8,mode)
        
        with self.assertRaises(Exception):
            SettingsHandler(9,mode)

        with self.assertRaises(Exception):
            SettingsHandler("0",mode)

        with self.assertRaises(Exception):
            SettingsHandler("0",mode)

        with self.assertRaises(Exception):
            SettingsHandler("0",mode)

        with self.assertRaises(Exception):
            SettingsHandler("0",mode)
        
    def test_day_key_as_integer_is_valid(self):
        try:
            SettingsHandler(0,mode)
        except Exception:
            assert False

        try:
            SettingsHandler(1,mode)
        except Exception:
            assert False

        try:
            SettingsHandler(2,mode)
        except Exception:
            assert False

        try:
            SettingsHandler(3,mode)
        except Exception:
            assert False

        try:
            SettingsHandler(4,mode)
        except Exception:
            assert False
        
        try:
            SettingsHandler(5,mode)
        except Exception:
            assert False

        try:
            SettingsHandler(6,mode)
        except Exception:
            assert False

    def test_restricted_time_segments(self):
        monday=SettingsHandler(0,mode)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(monday.get_restricted_time_segments(),expected_time_segments)

        tuesday=SettingsHandler(1,mode)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(tuesday.get_restricted_time_segments(),expected_time_segments)

        wednesday=SettingsHandler(2,mode)
        expected_time_segments=[(time(7,0),time(9,30)),(time(16,0),time(19,30))]
        self.assertEqual(wednesday.get_restricted_time_segments(),expected_time_segments)

        sunday=SettingsHandler(6,mode)
        self.assertEqual(sunday.get_restricted_time_segments(),[])

    
    def test_restricted_plate_ending_digits(self):

        monday=SettingsHandler(0,mode)
        expected_restricted_plate_ending_digits=[2,4,6,8,0]
        self.assertEqual(monday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        tuesday=SettingsHandler(1,mode)
        expected_restricted_plate_ending_digits=[1,3,5,7,9]
        self.assertEqual(tuesday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        wednesday=SettingsHandler(2,mode)
        expected_restricted_plate_ending_digits=[2,4,6,8,0]
        self.assertEqual(wednesday.get_restricted_plate_ending_digits(),expected_restricted_plate_ending_digits)

        sunday=SettingsHandler(6,mode)
        self.assertEqual(sunday.get_restricted_time_segments(),[])

        
      