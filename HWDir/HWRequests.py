

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_exchange_rate(from_currency, to_currency):
#     query = f"{from_currency} to {to_currency}"
#     url = f"https://www.google.com/search?q={query}"
#
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         return None
#
#     soup = BeautifulSoup(response.text, "html.parser")
#     rate_span = soup.find("span", class_="DFlfde", attrs={"data-precision": "2"})
#
#     if rate_span and 'data-value' in rate_span.attrs:
#         return float(rate_span['data-value'])
#
#     return None
#
#
# def convert_currency(amount, from_currency, to_currency):
#     rate = get_exchange_rate(from_currency, to_currency)
#     if rate:
#         return amount * rate
#     return "Не удалось получить курс валют"
#
# amount = 100
# from_currency = 'EUR'
# to_currency = 'JPY'
#
# result = convert_currency(amount, from_currency, to_currency)
# print(f"{amount} {from_currency} = {result:.2f} {to_currency}")