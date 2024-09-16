# 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
# 	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.
#
import re

pattern = r'#([A-Fa-f0-9]{6})'

text = "Цвета: Еще тЕксТ #ABCDEF, #AB3456, #AABBCC."
matches = re.findall(pattern, text)
print(matches)


# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)

pattern = r'(\d+)(?!\+)'

text = "2*9-6*5 (3+5)-9*4"
matches = re.findall(pattern, text)
print(matches)


# 3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время. [00:00 - 23:59]




text = "Завтрак в 09:00, а обед в 37:98 и ужин в 15:45. 16:60"

pattern = r'(?:[01]\d|2[0-3]):[0-5]\d'
matches = re.findall(pattern, text)
print(matches)

# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
# 	2) Все адреса

with open('people.txt', 'r', encoding='utf-8') as file:
    text = file.read()


name_pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
names = re.findall(name_pattern, text, re.MULTILINE)

address_pattern = r'\d{1,4} [A-Za-z\' ]+ St\., [A-Za-z\'\- ]+ [A-Z]{2} \d{5}'
addresses = re.findall(address_pattern, text)

print("Имена и фамилии:", names)
print("Адреса:", addresses)


# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.

pattern = r'^[a-zA-Z0-9]+$'

text = "Hello123"
if re.match(pattern, text):
    print("Строка состоит только из букв и цифр")
else:
    print("В строке есть другие символы")

# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)

pattern = r'^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{4}$'

isikukood = "39405270299"
if re.match(pattern, isikukood):
    print("Isikukood валиден")
else:
    print("Isikukood невалиден")

