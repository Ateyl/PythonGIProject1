import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('survey_results_public.csv')


def prof_and_hobb():
    hobbyists_count = df['Hobbyist'].value_counts()
    print("Количество программистов (профессионалы к хобби):")
    print(hobbyists_count)


def age_stat():
    age_series = df['Age'].dropna()
    avg_age = age_series.mean()
    max_age = age_series.max()
    min_age = age_series.min()

    print(f"Средний возраст: {avg_age:.2f} лет")
    print(f"Максимальный возраст: {max_age} лет")
    print(f"Минимальный возраст: {min_age} лет")


def countries_count():
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    country_counts = country_counts.sort_values(by='Count', ascending=False)

    print("страны по количеству программистов:")
    print(country_counts)


def currencies_count():

    currency_counts = df['CurrencyDesc'].value_counts().reset_index()
    currency_counts.columns = ['CurrencyDesc', 'Count']
    currency_counts = currency_counts.sort_values(by='CurrencyDesc', ascending=True)

    print("Валюты по алфавиту:")
    print(currency_counts)


while True:
    print("\nВыберите действие:")
    print("1 - Количество профессионалов и хобби-программистов")
    print("2 - Средний, максимальный и минимальный возраст программистов")
    print("3 - Таблица со странами")
    print("4 - Таблица с валютами")
    print("0 - Выйти")

    choice = input("выбери: ")

    if choice == '1':
        prof_and_hobb()
        age_stat()
    elif choice == '3':
        countries_count()
    elif choice == '4':
        currencies_count()
    elif choice == '0':
        print("Выход...")
        break
    else:
        print("попробуй снова")