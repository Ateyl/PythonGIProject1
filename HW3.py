# Print to console what is different in each set compared to another
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

diff_a = set_a - set_b  # or set_a.difference
print(diff_a)

diff_b = set_b-set_a
print(diff_b)

# Create a string from a list and save it to variable
# Make each name on a new line.
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']

names_string = '\n'.join(names)

print(names_string)


# print sum of all numbers in a list
# print sum of all unique numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]

sumNum = sum(numbers)

print(sumNum)

sumSet = sum(set(numbers))

print(sumSet)


# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']

list_all = list(set(studentsB+studentsA))

print(list_all)


# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)

inCommon = set(numbersA).intersection(set(numbersB))

print(inCommon)

# add 5 to the tuple on a right position
a = (1, 2, 3, 4, 6, 7, 8)

a_list= list(a)

a_list.insert(4,5)

new_tuple= tuple(a_list)

print(new_tuple)