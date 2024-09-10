# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке.



def clean_text (text):
    punct = '.,!?*;_'
    clean = ''
    for char in text:
        if char not in punct:
            clean += char.lower()

    return clean

with open('books.txt', 'r',encoding='utf8') as file:
    text = file.read()

proc_text = clean_text(text)

words = proc_text.split()
total_words = len(words)

un_words = set(words)
un_word_count = len(un_words)

sorted_un_words = sorted(un_words)

with open('books_out.txt' ,'w', encoding='utf8') as file:
    file.write(f'Всего слов: {total_words}\n')
    file.write(f'кол-во уникальных слов: {un_word_count}\n')
    file.write(f'Слова в алф. порядке: \n')
    for word in sorted_un_words:
        file.write(word + '\n')

print('Смотри books_out.txt')