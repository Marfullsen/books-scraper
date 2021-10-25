import csv
import requests
from bs4 import BeautifulSoup

# Const.
HOST = 'https://books.toscrape.com/'
DIR = 'catalogue/'

# Var.
i = 1
req = ''

# Fun.
def get_page(page):
  global req
  req = requests.get(f'{HOST}{DIR}{page}')
  return req.status_code

# Main
while get_page(f'page-{i}.html') != 404:
  soup = BeautifulSoup(req.text, 'lxml')
  book_link = soup.section.div.nextSibling.nextSibling.ol.li.h3.a.get('href')
  print(i, req.status_code, book_link)
  print(i, get_page(book_link))
  i += 1