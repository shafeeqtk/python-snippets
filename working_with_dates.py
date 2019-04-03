import datetime
from datetime import timedelta

today = datetime.datetime.now()
day = today.day
month = today.month
year = today.year

first_day_of_current_month = datetime.datetime(year, month, 1)

last_day_of_previous_month = first_day_of_current_month + timedelta(days=-1)
first_day_of_previous_month = datetime.datetime(last_day_of_previous_month.year, last_day_of_previous_month.month, 1)


last_day_of_previous_month_str = last_day_of_previous_month.strftime("%Y-%m-%d")
first_day_of_previous_month_str = first_day_of_previous_month.strftime("%Y-%m-%d")
