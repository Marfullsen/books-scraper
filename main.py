import requests
from bs4 import BeautifulSoup

# Const.
HOST = 'https://books.toscrape.com/'

# Var.
i = 1
req = ''

# Fun.
def get_page(i):
  global req
  req = requests.get(f'{HOST}catalogue/page-{i}.html')
  return req.status_code

while get_page(i) != 404:
  soup = BeautifulSoup(req.text, 'lxml')
  print(i, req.status_code)
  i += 1