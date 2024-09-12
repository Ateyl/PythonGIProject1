import itertools
from itertools import repeat

from JsonInPython.MainJson import people

# counter = itertools.count(100, -1)

# counter = itertools.cycle(['On', 'Off'])
# counter = itertools.repeat(0)   Повторяет

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
#
#
# x = [1,2,3]
# y = [4,5,6, 8]
# res = zip(x , y, counter)
# print(res)
# print(list(res))
#
# print(list(itertools.zip_longest(x,y)))


letter = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3,]

# NO ORDER, NO DUPLICATES
result = itertools.combinations(letter, 2)
for comb in result:
    print(comb)


print('\n')

# ORDER, NO DUPLICATES
result = itertools.permutations(letter, 2)
for comb in result:
    print(comb)

print('\n')

# ORDER, DUPLICATES
result = itertools.product(letter, repeat=2)
for comb in result:
    print(comb)

print('\n')

# NO ORDER, DUPLICATE
result = itertools.combinations_with_replacement(letter, 2)
for comb in result:
    print(comb)


numbers2 = [4,5,4,3,2,1,0,4]
selectors = [True, False, False, True]

result = itertools.compress(letter, selectors)
for item in result:
    print(item)

print('\n')

result = itertools.filterfalse(lambda x: x > 2, numbers2)
for item in result:
    print(item)

print('\n')

# result = itertools.dropwhile(lambda x: x > 2, numbers2)
result = itertools.takewhile(lambda x: x > 2, numbers2)
for item in result:
    print(item)

print('\n')


result = map(lambda x: x ** 2, numbers2)
for res in result:
    print(res)


print('\n')



people = [
    {
        'name': 'Jack',
    },
    {
        'name': 'Anton',
    },
    {
        'name': 'Ivan',
    }
]

def add_len(obj):
    return {
        'name': obj['name'],
        'name_length': len(obj['name']),
    }

result = map(add_len, people)
print(list(result))