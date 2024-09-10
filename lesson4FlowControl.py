# FLOW CONTROL
# IF ELSE, FOR, WHILE



# age = -1
# if age > 0:
#     if age <= 10:
#         print('He is child')
#     elif age <18:
#         print('He is teenager')
#     else:
#         print('He is adult')
# else:
#     print('incorrect input')
#
#
# print('Goodbye')
#
# username = input('Enter your useranme: ')
#
# if username:
#     print(f'Hello {username}')
# else:
#     print('Hello stranger')



#idcode = '38803160272' #
# idcode= input('Please input ID: ')
# if idcode.isdecimal():
#     print(idcode)
#     if len(idcode) != 11:
#         if len(idcode) < 11:
#             print('ID code is too short')
#         else:
#             print('your ID is too long')
#         print('ID length is not 11 digits long')
#     else:
#         print('ID is correct')
# else:
#     print('ID you entered is nit numeric')


# x = True
# x and print('Hello world')


# age = 20
#
# if age <= 10 and age > 0:
#     print('He is child')
# if age <18 and age > 10:
#     print('He is teenager')
# if age >=18:
#     print('He is adult')


numbers = range(0,101) # if instead of numbers we put in letters THE LETTER PY will check every letter
# print(numbers)
odds = []
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else: odds.append(num)

print(odds)
print(evens)


names = ['Jack', 'Artyom', 'Sara', 'Ivan', 'Anton']

for name in names:
    print(f'Hello {name}')




people = [
    ['Jack', 34, 'm'],
    ['Artyom', 23, 'm'],
    ['Sara', 20, 'f'],
    ['Ivan', 30, 'm'],
    ['Anton', 25, 'm'],
]

for person in people:
    if person[2] == 'm':
        print(f'This is {person[0]} he is {person[1]} years old')
    elif person[2] == 'f':
        print(f'This is {person[0]} she is {person[1]} years old')


for name, age, gender in people:
    if gender == 'm':
        print(f'This is {name} he is {age} years old')
    elif gender == 'f':
        print(f'This is {name} she is {age} years old')


# range(10) => [ 0 1 2 3 4 5 6 7 8 9]
for num1 in range(10):   # 10
    for num2 in range(10):   # 100
        for num3 in range(10):   # 1000
            for num4 in range(10):   # 10000
                print(num1, num2, num3, num4)



# для диапозона чисел от 1 до 100 включительно
# если число делится на 3 без остатка вывести число и FIZZ
# если число делится на 5 без остатка вывести число и BUZZ
# если число делится на 3 и на 5 без остатка вывести число и FIZZBUZZ
# каждое число выводится не больше одного раза