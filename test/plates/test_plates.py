from unittest import TestCase
from src.subdomains.plate import LicensePlate

class TestPlatesSubdomain(TestCase):
    def test_plate_data_type_is_incorrect(self):
        with self.assertRaises(Exception):
            LicensePlate("T*V-12345")

        with self.assertRaises(Exception):
            LicensePlate("78J-123F")

        with self.assertRaises(Exception):
            LicensePlate("*-+-12345")

        with self.assertRaises(Exception):
            LicensePlate("AAAA-123456")

        with self.assertRaises(Exception):
            LicensePlate("aaa1234")

        with self.assertRaises(Exception):
            LicensePlate("AAA1234")

        with self.assertRaises(Exception):
            LicensePlate("1231234")

        with self.assertRaises(Exception):
            LicensePlate("AAA-34**")

        with self.assertRaises(Exception):
            LicensePlate("")

        with self.assertRaises(Exception):
            LicensePlate(None)

    def test_plate_data_type_is_correct(self):
        try:
            LicensePlate("TBF-1234")
        except Exception:
            assert False

        try:
            LicensePlate("PTT-123")
        except Exception:
            assert False

        try:
            LicensePlate("AAA-0826")
        except Exception:
            assert False

        try:
            LicensePlate("AAA-4666")
        except Exception:
            assert False

    def test_retrive_plate_last_digit(self):
        plate1=LicensePlate("TBF-1234")
        self.assertEqual(plate1.get_last_digit(),4)

        plate2=LicensePlate("PTT-123")
        self.assertEqual(plate2.get_last_digit(),3)

        plate3=LicensePlate("AAA-0826")
        self.assertEqual(plate3.get_last_digit(),6)

        plate4=LicensePlate("TBD-4668")
        self.assertEqual(plate4.get_last_digit(),8)

        plate5=LicensePlate("QTY-4660")
        self.assertEqual(plate5.get_last_digit(),0)

        plate6=LicensePlate("LKJ-660")
        self.assertEqual(plate6.get_last_digit(),0)
    