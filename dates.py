from datetime import date


def day_of_the_week_month_start(year_number, month_number):
    return day_of_the_week(year_number, month_number, 1)


def day_of_the_week(year_number, month_number, day_number):
    test_date = date(year_number, month_number, day_number)
    return test_date.strftime('%A')


def has_Friday_Thirteenth(year_number, month_number):
    test_date = date(year_number, month_number, 13)
    if test_date.strftime('%A') == "Friday":
        return True
    else:
        return False
