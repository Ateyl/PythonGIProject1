# 'r' - read
# 'w' - write   !!! Стирает файл при открытии
# 'a' - append
# 'x' - create
# 'r+' - read and write

# C:\Users\Ateyl\PycharmProjects\pythonGIProject1\Tester\Lesson8workingWithFiles.py
# Lesson8workingWithFiles.py

# with open(r'../test.txt', 'r', encoding='utf8') as file:
#     print(file.closed)
# print(file.closed)

# with open(r'../test.txt', 'r', encoding='utf8') as file:
    # data = file.read()
    # print(data)
    # file.seek(0)
    # data2 = file.read()
    # print(len(data2))
#     data = file.readline()
#     print(data)
#     data2 = file.readline()
#     print(data2)
#
# data = file.readline()
# print(data)
# while len(data) > 0:
#     data = file.readline()
#     print(data)


# with open(r'../test.txt', 'r', encoding='utf8') as file:
#     data = file.read()
    # print(data)
    # file.write(' some    spaces ')
    # file.seek(0)
    # file.write(data.upper())
    # print(data)

#
# data = data.lower()
# with open(r'../test.txt', 'w', encoding='utf8') as file:
#     file.write(data)
#

with open('../MountainsAndSea.jpg', 'rb') as file:
    data = file.read()
    print(data)
    print(data)
    with open('../MountainsAndSea_copy.jpg', 'wb') as file2:
        file2.write(data)
# print(file)
# print(file.encoding)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)