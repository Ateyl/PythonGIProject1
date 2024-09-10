# Практикум 1:
#
#     1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#         Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

name = input('Hello, please enter your name: ')
surname = input('enter your surname: ')
age = input('Enter yor age: ')

print(f'Hello, {surname} {name}. Your age is: {age}.')


#     2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (
#     с = sqrt(a * a  +  b * b))

a = float(input('введите длину 1 катета: '))
b = float(input('введите длину 2 катета: '))

c = (a* a+ b * b) ** 0.5
print(c)

#
#     3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет,
#     является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5

a = float(input('введите a: '))
b = float(input('введите b: '))
c = float(input('введите c: '))

max_side = max(a, b, c)

if max_side == a:
   right_triangle = a**2 == c**2 +b**2
elif max_side == b:
    right_triangle = b**2 == c**2 + a**2
elif max_side == c:
    right_triangle = c**2 == b**2 +a**2

if right_triangle:
    print('Это прямоугольный треугольник')
else:
    print('это не прямоугольный треугольник')



#     4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке.

userList =[]

userList.extend(input('введите то, что должно быть в листе, разделяя пробелами: ').split())
reverse_list = userList[::-1]
print('элементы в обратном порядке: ', reverse_list)

# или

user_list = input('Введите элементы списка, разделенные пробелами: ').split()
reversed_list = user_list[::-1]
print("Элементы списка в обратном порядке:", reversed_list)



#
#     5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#         Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

tupleA = (1,2,3,4,5,)
tupleB = (8,2,5,)
listA = list(tupleA)
listA.insert(2, tupleB)
tupleA = tuple(listA)
print(tupleA)

# или

listA = list(tupleA)
listA[2:2] = tupleB
tupleA = list(listA)
print(tupleA)




#     6 *Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#         Примеры:
#         [1, 2, 3, 4, 7, 9, 9] → [9]
#         [1, 2, 4, 6, 4, 6] → [4,6]

# test_lst = [1,2,2,3,3,3,4,4,5,5,6,6,6]
# max_count = 0
# result =[]
#
# for number in test_lst:
#    if test_lst.count(number) > max_count(number):
#        max_count = test_lst.count(number)
#
# for number in test_lst:
#     if test_lst.count(number) == max_count:
#         if number not in result:
#             result.append(number)
#
# print(result)


test_lst = [1,2,2,3,3,3,4,4,5,5,6,6,6]
result = {}

for number in test_lst:
    result[number] = test_lst.count(number)
print(result)
res = []
for key in result.keys():
    if result[key] == max(result.values()):
        res.append(key)
print(result)


#
#     7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#         Примеры:
#         1234565 seconds = 14:6:56:5

def time_format(seconds):
    sec_in_min = 60
    min_in_hour = 60
    hour_in_day = 24

    abs_sec = abs(seconds)

    days = abs_sec // (sec_in_min * min_in_hour * hour_in_day)
    rem_sec = abs_sec % (sec_in_min * min_in_hour * hour_in_day)

    hours = rem_sec // (sec_in_min * min_in_hour)
    rem_sec %= (sec_in_min * min_in_hour)

    mins = rem_sec // sec_in_min

    seconds = rem_sec % sec_in_min

    return f'{days}:{hours}:{mins}:{seconds}'
while True:
    try:
        total_sec = int(input('напишите время в секундах: '))
        formatted_time = time_format(total_sec)
        if total_sec < 0:
            print(f'{total_sec} seconds = T-: {formatted_time}')
        else:
            print(f'{total_sec} seconds = T+: {formatted_time}')
            break


    except ValueError:
        print('Нужно использовать только цифры!')


