import html
from http.client import responses

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as BS

# 200 - success
# 300 - redirect
# 400 - client error
# 500 - server error

# r = requests.get('https://xkcd.com/353/', timeout=20)
# print(r.cookies)


try:
    response = requests.get('http://github.com', timeout=20)
    response.raise_for_status()
except HTTPError as err:
    print(f'HTTP error: {err}')
else:
    print('success')


url = 'https://www.gammatest.net/ru/kurs_python_105.php'
response = requests.get(url, timeout=20)
soup = BS(response.content, 'html.parser')
print(soup.title.text)
match = soup.find('div', id='fb-root')
match = soup.find_all('a')
print(match)
for m in match:
    print(m.get_attribute_list('href'))

row = match.findParent()

response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=20) #также работают ost get delete  и тд
result = response.json()
for post in result:
    print(post['title'])
    print(post['body'])
    print('*' * 20)