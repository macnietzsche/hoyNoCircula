from unittest import TestCase
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

        
      