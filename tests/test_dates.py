import unittest
from dates import *


class TestDates(unittest.TestCase):

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

    def test_day_name_locale(self):
        english = day_of_week_in_locale(2021, 3, 30, 'en_GB')
        print("UK locale is: " + english)
        self.assertEqual("Tuesday", english)

        french = day_of_week_in_locale(2021, 3, 30, 'fr_FR')
        print("French locale is: " + french)
        self.assertEqual("mardi", french)

        german = day_of_week_in_locale(2021, 3, 30, 'de_DE')
        print("German locale is: " + german)
        self.assertEqual("Dienstag", german)

    def test_Friday_Thirteenth(self):
        self.assertTrue(has_friday_thirteenth(2020, 11))
        self.assertFalse(has_friday_thirteenth(2020, 12))

    def test_Friday_Thirteenths_this_year(self):
        self.assertEqual(1, friday_thirteenths_this_year(2016))
        self.assertEqual(2, friday_thirteenths_this_year(2020))
        self.assertEqual(3, friday_thirteenths_this_year(2015))
