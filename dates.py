from datetime import date
from babel.dates import format_date

def day_of_the_week_month_start(year_number, month_number):
    return day_of_the_week(year_number, month_number, 1)


def day_of_the_week(year_number, month_number, day_number):
    test_date = date(year_number, month_number, day_number)
    return test_date.strftime('%A')


def has_friday_thirteenth(year_number, month_number):
    test_date = date(year_number, month_number, 13)
    if test_date.strftime('%A') == "Friday":
        return True
    else:
        return False


def day_of_week_in_locale(year_number, month_number, day_number, locale_string):
    test_date = date(year_number, month_number, day_number)
    # locale_day = format_date(test_date, format='full', locale=locale_string)
    locale_day = format_date(test_date, "EEEE", locale=locale_string)
    return locale_day


def friday_thirteenths_this_year(year_number):
    # always 1-3, never 0 or 4
    month = 1
    thirteenths = 0
    while month < 13:
        if has_friday_thirteenth(year_number, month):
            thirteenths = thirteenths + 1
        month = month + 1
    return thirteenths
