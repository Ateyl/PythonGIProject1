"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object

import datetime  #or from datetime import * не надо упоминать datetime


sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

print(datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p'))

def convert_to_datetime(date_string):

    for form in [
        '%b %d %Y %I:%M%p',
        '%H:%M %y/%m/%d',
        '%A, %B %d, %Y',
        '%d.%m.%Y - %H:%M:%S'
    ]:
        try:
            return datetime.datetime.strptime(date_string, form)
        except ValueError:
            pass
    return



# Write a program to print yesterdays, today and tomorrow dates

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)


print("Yesterday's date:", yesterday)
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200

date_object = datetime.datetime.fromtimestamp(some_day)
formatted_object = date_object.strftime('%d.%m.%Y')
print(formatted_object)




# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)


def subtract_two_weeks(timestamp):
    date_obj = datetime.datetime.fromtimestamp(timestamp)
    new_date = date_obj - datetime.timedelta(weeks=2)
    new_timestamp = new_date.timestamp()
    return new_timestamp

input_stamp = float(input('Enter timestamp: '))

new_stamp = subtract_two_weeks(input_stamp)

print('Output timestamp: ', new_stamp)


# Enter timestamp: 1014163200.0
# Output timestamp:  1012953600.0