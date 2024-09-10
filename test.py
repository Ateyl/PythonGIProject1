#  Вычисляет возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)


# years

# current_year = 2023
# year_of_birth = 1988
#
#
# w = str(current_year - year_of_birth)
# print(w)

# 2. Найти недостающую часть кода (code_2):
#    - найдите остаток от x деленого на y
#    - полученый результ умножьте на 13
#    - извлеките квадратный корень из полученного результата (аналогично возведению в степень 0.5)
#    - возьмите целую часть от результата

# code 2 data
# x = 152
# y = 132
#
# z = x % y
#
# print(z)
#
# z *= 13
#
# print(z)
#
# z **= 0.5
#
# print(z)
#
# print(int(z))   #or // 1

# 3. Соединить код в отдельную переменную
# пример:
# 475-12-967
# 4. Вывести строку используя доступные переменные:
# пример:
# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.

# code parts
# code_1 = '354'
# code_3 = 132
#
# # name
# user_name = 'John'
# user_surname = 'Smith'
#
#
#
# print('Hello',user_name + " " + user_surname + '.' + ' You are ' + w + ' years old.' + ' Your secret code is ' + code_1 + '-16-' + str(code_3))


# while input :
#     print('I cant stop')

#





# import functions as mf
# print(mf.FF(123))
#
#
# from functions import FF as ff
#
# print(ff(123))
#



# listA = list(tupleA)
# listA.insert(2, tupleB)
# tupleA = tuple(listA)
# print(tupleA)
#
# # или

#
# tupleA = (1,2,3,4,5,)
# tupleB = (8,2,5,)
#
# listA = list(tupleA)
# listA[2:2] = tupleB
# tupleA = list(listA)
# print(tupleA)


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


