from unittest import TestCase
from src.predictor.predictor import Predictor

mode="testing"
class TestPredictor(TestCase):
    def test_can_my_vehicle_be_on_the_road(self):
        #Test when not in restricted hours
        test=Predictor("2020-12-01 15:23","AAA-0826",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2020-12-01 10:23","AAA-0821",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2020-12-01 12:23","AAA-0820",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        #Test when on Sundays
        test=Predictor("2021-08-01 15:23","AAA-0826",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2021-09-19 08:00","AAA-0826",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2023-10-15 17:10","AAA-0826",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        #Test restricted plates on MO,WED,WED
        test=Predictor("2021-08-02 08:23","AAA-0820",mode)
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2021-09-15 16:33","AAA-0826",mode)
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2023-10-27 07:00","AAA-0828",mode)
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        #Test not restricted plates on MO,WED,WED
        test=Predictor("2021-08-02 08:23","AAA-0821",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2021-09-15 16:43","AAA-0823",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2023-10-27 18:23","AAA-0825",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        #Test restricted plates on TU,TH,SA
        test=Predictor("2021-08-21 7:00","AAA-0821",mode)
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2021-09-11 16:00","AAA-0823")
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2023-10-07 19:30","AAA-0825",mode)
        self.assertFalse(test.can_my_vehicle_be_on_the_road())

        #Test not restricted plates on TU,TH,SA
        test=Predictor("2021-08-21 7:00","AAA-0822",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2021-09-11 16:00","AAA-0820",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())

        test=Predictor("2023-10-07 19:30","AAA-0826",mode)
        self.assertTrue(test.can_my_vehicle_be_on_the_road())