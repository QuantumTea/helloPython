import unittest
from dates import *


class TestMaths(unittest.TestCase):

    def test_first_day_of_month(self):
        result = day_of_the_week_month_start(2020, 1)
        print("1/1/2020 is a " + result)
        self.assertEqual("Wednesday", result)

        result2 = day_of_the_week_month_start(2000, 1)
        print("1/1/2000 is a " + result2)
        self.assertEqual("Saturday", result2)

    def test_day_of_week(self):
        result = day_of_the_week(1969, 10, 31)
        print("10/31/1969 is a " + result)
        self.assertEqual("Friday", result)

        result2 = day_of_the_week(2017, 10, 12)
        print("10/12/2017 is a " + result2)
        self.assertEqual("Thursday", result2)

    def test_Friday_Thirteenth(self):
        self.assertTrue(has_Friday_Thirteenth(2020, 11))
        self.assertFalse(has_Friday_Thirteenth(2020, 12))
