"""
Это можно использовать как блочный коментарий
"""
from itertools import count

string_sample1 = 'Hello world world'

string_sample2 = 'fiRSt LEtteR Is loweCASE'

string_sample3 = '     extra   whitespace'

german_sample = ' der Fluß'

# print(''' запоминает
# форматирование текста   ''')

print(string_sample1[16])

print(len(string_sample1))

print(string_sample1[6:12])  # or [5:] он возмёт последний индекс [START:END] END не включён

print(string_sample1[:5])
print(string_sample1[5:])
print(string_sample1[5:15:3])  # [from:TO:step]
print(string_sample1[::2])
print(string_sample1[::-1])  # [::-1] самый простой способ перевернуть строку

print(string_sample1.upper())

print(german_sample.lower())

print(german_sample.casefold())

print(string_sample2.capitalize())  # первая буква теперь заглавная

print(string_sample2.title())     # каждая первая буква теперь заглавная, подходит для ввода имен

print(string_sample1.istitle())

print(string_sample3.strip(' '))  # .STRIP обрезает края

print(string_sample1.replace('world', 'planet', 1 ))
print(string_sample1.replace(' ', '', 1))

print(string_sample1.count('world', 3,12))
print(string_sample1.find('world', 5,16))
print(string_sample1[6:])
print('Hello'.center(20, '*'))

salary = 1000
string = 'John salary is {0}.{1}'
print(string.format(salary, True))

string = 'This {product} costs {price:.2f}$.'

print(string.format(product='computer', price=1000))

name = 'jack'
surname = 'smith'
salary = 1500
print(f'This is {name.title()} {surname.title()}. {name.title()}`s salary is {salary}$.')

print(len('That\'s'))
print("My favourite book is \"Metro 2033\"")

print('\thello\\n world')

print()