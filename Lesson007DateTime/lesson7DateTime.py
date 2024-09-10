#libraries

import calendar
from datetime import timedelta

# print(calendar.calendar(2024,w=5, l=0, c=6, m=2))

# print(calendar.month(2024,9, 5,0))
# print(calendar.isleap(2024))
# print(calendar.leapdays(2000, 2025))


import time
#
# print(time.time())
# start = time.time()
# print('hello world')
# # time.sleep(10)
# print(time.localtime())
# stop = time.time()
# print(stop - start)


import datetime
#
# d = datetime.date(2024, 9, 1)
# print(d.day)
# print(d.month)
# print(d)
# print(type(d))
# today = datetime.date.today()
# print(today)
# print(today.weekday())
# print(today.isoweekday())
#
# if today.isoweekday() in [6,7]:
#     print('weekend')
# else:
#     print('workday')


# if date1 -date2 = timedelta
#date1 + timedelta = date2
#
# diff = today - d
# print(diff)
# print(type(diff))
#
# tdelta = datetime.timedelta(hours=18, minutes=33)
#
# print(today + tdelta)
# print(tdelta.total_seconds())


# t = datetime.time(12, 43, 17)
# print(t.hour)
# print(type(t))
# dt = datetime.datetime(2024,9,4, 18,30,15)
# print((dt - tdelta).time())
# print(type(dt))
# today = datetime.datetime.today()
# print(today)

# today = datetime.datetime.today()
#
# print(today.strftime('%d %B %Y'))

# date_str = 'September 4 2024 Wed, 20:30:15'
# dt = datetime.datetime.strptime(date_str, '%B %d %Y %a, %H:%M:%S')
# print(dt)


today = datetime.datetime.today()
print(today.timestamp())
ts = 1725471988.705424
new_datetime = datetime.datetime.fromtimestamp(ts)
print(new_datetime)