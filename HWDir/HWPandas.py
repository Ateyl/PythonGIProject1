import pandas as pd

df = pd.read_csv('survey_results_public.csv')

df['IsHobbyist'] = df['CodingActivities'].astype(str).str.contains('Hobby', case=False, na=False)

def parse_age(age_str):
    if pd.isna(age_str):
        return None
    age_str = age_str.lower()
    if 'under 18' in age_str:
        return 17
    elif '18-24' in age_str:
        return 21
    elif '25-34' in age_str:
        return 29.5
    elif '35-44' in age_str:
        return 39.5
    elif '45-54' in age_str:
        return 49.5
    elif '55-64' in age_str:
        return 59.5
    elif '65 or older' in age_str or '65+' in age_str:
        return 70
    else:
        return None

df['AgeNumeric'] = df['Age'].apply(parse_age)

while True:
    print("\nВыберите:")
    print("1 - Количество профф., и хобби программистов")
    print("2 - Средний, максимальный и минимальный возраст программистов")
    print("3 - Количество программистов по странам")
    print("4 - Количество программистов по валютам")
    print("0 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        hobbyists = df['IsHobbyist'].sum()
        professionals = len(df) - hobbyists
        print("\nКоличество программистов:")
        print(f"Хобби-программисты: {hobbyists}")
        print(f"Профессиональные программисты: {professionals}")

    elif choice == '2':
        age_numeric = df['AgeNumeric'].dropna()
        if age_numeric.empty:
            print("\nНет доступных данных.")
        else:
            avg_age = age_numeric.mean()
            max_age = age_numeric.max()
            min_age = age_numeric.min()
            print("\nСтатистика по возрасту:")
            print(f"Средний возраст: {avg_age:.2f} лет")
            print(f"Максимальный возраст: {int(max_age)} лет")
            print(f"Минимальный возраст: {int(min_age)} лет")

    elif choice == '3':
        if 'Country' in df.columns:
            country_counts = df['Country'].value_counts().sort_values(ascending=False)
            print("\nКоличество программистов по странам:")
            print(country_counts)
        else:
            print("\n Столбец 'Country' не найден.")

    elif choice == '4':
        currency_column = 'CurrencyDesc' if 'CurrencyDesc' in df.columns else 'Currency'
        if currency_column in df.columns:
            currency_counts = df[currency_column].value_counts().sort_index()
            print(f"\nКоличество программистов по валютам ({currency_column}):")
            print(currency_counts)
        else:
            print("\nСтолбец с валютами не найден.")

    elif choice == '0':
        print("Выход...")
        break

    else:
        print("попробуй снова.")