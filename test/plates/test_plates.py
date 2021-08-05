from unittest import TestCase
from src.subdomains.plate import LicensePlate

class TestPlatesSubdomain(TestCase):
    def test_plate_data_type_is_incorrect(self):
        incorrect_plates=["T*V-12345","78J-123F","*-+-12345,AAAA-123456","aaa1234","AAA1234","1231234","AAA-34**"]
        with self.assertRaises(Exception):
            for incorrect_plate in incorrect_plates:
                LicensePlate(incorrect_plate)

    def test_plate_data_type_is_correct(self):
        correct_plates=["TBF-1234","PTT-123","AAA-0826","AAA-4666"]
        for correct_plate in correct_plates:
            try:
                LicensePlate(correct_plate)
            except Exception:
                assert False
    