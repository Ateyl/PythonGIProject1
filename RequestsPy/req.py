from http.client import responses

import requests
from requests.exceptions import HTTPError

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