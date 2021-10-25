import csv
import requests
from bs4 import BeautifulSoup

# Const.
HOST = 'https://books.toscrape.com/'
DIR = 'catalogue/'

# Var.
i = 1
req = ''
line_count = 0

# Fun.
def get_page(page):
  global req
  req = requests.get(f'{HOST}{DIR}{page}')
  return req.status_code

def create_csv_file():
  with open('scraped_books.csv', mode='w') as scraped_books:
    fieldnames = ['Title',
      'Price',
      'Stock',
      'Category',
      'Cover',
      'UPC',
      'Product Type',
      'Price (excl. tax)',
      'Price (incl. tax)',
      'Tax',
      'Availability',
      'Number of reviews'
      ]
    writer = csv.DictWriter(scraped_books, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()

def write_to_csv():
  global line_count
  line_count += 1

# Main

# Se inicia el proyecto con una hoja CSV nueva.
create_csv_file()

while get_page(f'page-{i}.html') != 404:
  soup = BeautifulSoup(req.text, 'lxml')
  books = soup.section.div.nextSibling.nextSibling.ol.findAll('li')
  for n, book in enumerate(books):
    print(n, book.h3.a.get('href'))
  #book_link = soup.section.div.nextSibling.nextSibling.ol.li.h3.a.get('href')
  #print(i, req.status_code, book_link)
  #print(i, get_page(book_link))
  i += 1

print(f'Se procesarion {line_count} libros.')