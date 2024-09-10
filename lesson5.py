from random import triangular


# while True:
#     idcode = '38803160272' #
#     idcode= input('Please input ID: ')
#     if idcode.isdecimal():
#         print(idcode)
#         if len(idcode) != 11:
#             if len(idcode) < 11:
#                 print('ID code is too short')
#                 continue
#             else:
#                 print('your ID is too long')
#             continue
#         else:
#             while True:
#                 name = input('Enter name: ')
#                 if not name:
#                     print('Try again!')
#                     continue
#                 break
#                 # exit()  --- методы закрывают программу
#                 # quit()  ---
#             break
#     else:
#         print('ID you entered is nit numeric')
#         continue
# print('Good bye!')










# try:
#     name = input('Enter name: ')
#     if not name:
#         raise Exception
#
# except ValueError:
#     print('can\'t convert to int ERROR')
#
# except ZeroDivisionError:
#     print('Dont divide by 0')
# except Exception:
#     print('name is empty')
# else:
#     print('No error')
#
#
# finally:
#     print('Good bye!')





def say_hello(name, surname):
    return f'hello {name} {surname}!'

x = say_hello('Roman', 'Kutselepa')


# say_hello('Artyom')                        # --- () argument = parameter
# say_hello('Marry')
# say_hello('Roman')                        # --- () argument = parameter
# say_hello('Alex')

print(x)


# y = []
# def add_to_x(value):
#     if value:
#         x.append(value)
#
#
# add_to_x('Hello')
# add_to_x('World')
# print(y)


# say_hello('Artyom')                        # --- () argument = parameter
# say_hello('Marry')
# say_hello('Roman')                        # --- () argument = parameter
# say_hello('Alex')


#
# def short_to_long(string):
#     if len(string) > 5:
#         return 'long'
#     else:
#         return 'short'
#     print('Goodbye')
#
# print(short_to_long('11111'))
#
#
# words = ['Sun', 'Earth', 'MIllenium', 'Star']
#
# for word in words:
#     print(short_to_long(word))


#
#
# def fizz_buzz(start, end):
#     for num in range(start, end + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print(num , 'fizzbuzz')
#         elif num % 3 == 0:
#             print(f'{num} fizz')
#         elif num % 5 == 0:
#             print(num, 'Buzz')
#
# fizz_buzz(-100, 2000)

#
# a = 1
# b = 2
# c = 3
#
#
# def sample():
#     global a, b
#     a = 10
#     b = 20
#     c = 30
#     print(a, b, c)
#
#
# sample()
# print(a ,b ,c)


# a = 100
#
# def sample(a):
#     print(a ** 2)
#
# sample(12)
# print(a)



a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

def tri_area(a, b ,c):
    p = (a + b + c) / 2
    area = (p *(p - a) *(p - b)* (p - c)) ** 0.5
    return area


print(tri_area(a,b,c))    #  МОЖНО ЗАМЕНИТЬ НА a b c ТАК КАК Я ПОСТАВИЛ a b c НА INPUT

def print_result():
    print(f'The area of triangle is {tri_area(a,b,c)} cm2')


print_result()

# РАБОТА В НИДЕРЛАНДАХ