# Для диапозона чисел от 1 до 100 включительно
# Если число делится на 3 без остатка, вывести число и FIZZ
# Если число делится на 5 без остатка, вывести число и BUZZ
# Если число делится на 3 и на 5 без остатка, вывести число и FIZZBUZZ
# Каждое число выводится не больше одного раза

numbers = list(range(1, 101))
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} FIZZBUZZ')
    elif num % 3 == 0:
        print(f'{num} FIZZ')
    elif num % 5 == 0:
        print(f'{num} BUZZ')


print('Test')