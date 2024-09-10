from mimetypes import add_type
from sys import set_int_max_str_digits

# empty = []
# Empty = list()
# print(type(empty)) # list()
# print(bool(empty)) # empty list give false value
# x=3
# filled = [123, 0.123, 'hello', x, [1,2,[3,4,5],6],True, True,True]
#
# print(len(filled))
# print(filled[4][2][1])
#
# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', '1234567890']
#
# print(courses[1:4])
# print(courses[::-2]) # [START:END:STEP]
#
# courses[0] = 'Art1'
# courses.append('Art2')
# print(courses)
#
# courses.insert(0,'English')
# courses.extend(['Art3', 'Economics',])
# print(courses)

#courses.remove('Math')
#print(courses)




# print(courses.pop(0))
# print(courses)
#
# courses.reverse()
# print(courses)
#
# courses.sort()
# print(courses)
# print(courses[2])
#
# numbers = [45,23,54,23.23]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
#
# print(min(courses))
# print(max(courses))
# print(min('Hello world'))
# print(max('Hello world'))
# # print(sum(courses))
#
# print('Math' in courses)
#
# print('hello people of planet earth'.split())

#user_input = input('Enter something: ')
#print(user_input.split(', '))    #$ что бы мы не писали в input всегда возвращает строку
#sep = 123
#print(str(sep).join(courses))

#a = "one"
#b = a
#a+="two"
#print(a,b)

# a = [1,2,3,4,5]
# b = a.copy()
# a.append(555)
# b.append(777)
# print(a)
# print(b)
#
#

#pty = ()
# pty = tuple()
# print(type(pty))  # tuple()
#
# x = (1,)
# print(type(x))
#
# courses = ('History', 'Math', 'Literature', 'Physics', 'Programming', '1234567890')
# print(courses[0])
# print(courses.count('Math'))
# print(courses.index('Math'))
#
# u = 12,23,45,77
# print(u)
# courses = list(courses)
# print(courses)
# courses.append('Art4')
# courses = tuple(courses)
# print(courses)
#
#
# print([1,2,3]+ [4, 7,9]) # = list
# print((1,2,3)+ (5,2,1))  # = tuple
#
#
# z = set() #set()
# print(type(z))
#
# cour = {'History', 'Math', 'Literature', 'Physics', 'Programming', '1234567890'}
# print(cour)
#
# courses2 = {'Math', 'Economics', 'History', 'Spanish'}
#
# print(cour.difference(courses2))
# print(courses2.difference(cour))
# print(cour.intersection(courses2))
#



                  # DICT



# empty = dict()
# print(type(empty))
#
# x = 5
# sample = {
#     'name': 'Jack',
#     'courses': ['Art' , 'English', 'Programming'],
#     12: 'int key',
#     0.2: 'float key',
#     x: 'variable key',
#     'dictinary': {'name': 'bob', 'surname': 'Smith'},
#
# }
#
# # print(sample['courses'])
# print(sample['dictinary'].get('name', [])) # через метод get не будет ошибки
# sample['name'] = 'Sarah'
# sample['phone'] = '569-555-5555'
# print(sample)
#
# sample.update({'name': 'Bob', 'address': 'Tallinn',})
#
# # sample['dictinary'].update({'name': 'Alice', 'surname': 'Johnson'})  ---  can update in a few ways
#
# # sample['dictinary']['name'] = 'Alice' ---
# # sample['dictinary']['surname'] = 'Johnson' ---
#
#
# print(sample)
#
# # del sample['name']
# # print(sample)
#
# d1 = sample.pop('courses')
# print(d1)
# print(sample)


sample2 = {'name': 'Jack', 'surname': 'Smith', 'age': 41,}

for x in sample2:
    print(sample2[x])


print(sample2.keys())
print(sample2.values())
print(sample2.items())

for k, v in sample2.items():
    print(k, v)


