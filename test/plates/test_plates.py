from unittest import TestCase
from src.subdomains.plate import LicensePlate

class TestPlatesSubdomain(TestCase):
    def test_plate_data_type_is_incorrect(self):
        incorrect_plate="T*V-12345"
        with self.assertRaises(Exception):
            LicensePlate(incorrect_plate)

    def test_plate_data_type_is_correct(self):
        correct_plate="TBB-12345"
        try:
            LicensePlate(correct_plate)
        except Exception:
            assert False
    