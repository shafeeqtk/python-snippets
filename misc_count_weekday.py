# Identify which weekday would the first of month fall on, for the next N months. 
# N is set with months_into_future variable.
# Here, we count the sundays in the next 36 months

from datetime import datetime
from dateutil.relativedelta import relativedelta

months_into_future = 36 

iso_weekdays = {
    1:"Monday", 
    2:"Tuesday", 
    3:"Wednesday",
    4:"Thursday", 
    5:"Friday", 
    6:"Saturday",
    7:"Sunday"
}

count_map = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.today()
ymd1 = datetime(year=today.year, month=today.month, day=1)

ymd1

count = 0
for i in range(0,months_into_future):
    ymd_future = ymd1 + relativedelta(months=i)
    print(ymd_future.year, ymd_future.month, ymd_future.day, ":", iso_weekdays[ymd_future.isoweekday()])
    ymd_future.month
    count_map[ymd_future.isoweekday()] += 1

        
for k in count_map.keys():
    print(f"{count_map[k]} {iso_weekdays[k]} in the next {months_into_future} months")
