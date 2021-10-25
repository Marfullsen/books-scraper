import csv
import requests
from bs4 import BeautifulSoup

# Const.
CSV_FILENAME = 'scraped_books.csv'
DELIMITER = ';'
QUOTECHAR = '"'
HOST = 'https://books.toscrape.com/'
DIR = 'catalogue/'

# Var.
i = 1
req = ''
line_count = 0

# Anonf.
only_num = lambda s: ''.join([i for i in s if i.isdigit()])

# Fun.
def get_page(page):
  global req
  req = requests.get(f'{HOST}{DIR}{page}')
  return req.status_code

# Mod.
def create_csv_file():
  with open(CSV_FILENAME, mode='w', newline='') as scraped_books:
    fieldnames = ['Title',
      'Price (pounds)',
      'Stock',
      'Category',
      'Cover',
      'UPC',
      'Product Type',
      'Price in pounds (excl. tax)',
      'Price in pounds (incl. tax)',
      'Tax (pounds)',
      'Availability',
      'Number of reviews'
      ]
    writer = csv.DictWriter(scraped_books, delimiter=DELIMITER, quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
    writer.writeheader()

def write_to_csv(scraped_book_info):
  global line_count
  with open(CSV_FILENAME, mode='a', encoding="utf-8", newline='') as scraped_books:
    writer = csv.writer(scraped_books, delimiter=DELIMITER, quotechar=QUOTECHAR, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(scraped_book_info)
  line_count += 1

def init():
  # Se inicia el proyecto con una hoja CSV nueva.
  create_csv_file()

# Main
init()

while get_page(f'page-{i}.html') != 404:
  print(f'Página {i}')
  soup = BeautifulSoup(req.text, 'lxml')
  books = soup.section.div.nextSibling.nextSibling.ol.findAll('li')
  for n, book in enumerate(books):
    book_req = get_page(book.h3.a.get('href'))
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.find("h1").text
    price = soup.find(attrs={"class":"price_color"}).text[2:]
    stock = only_num(soup.find(attrs={"class":"instock availability"}).text.strip())
    category = soup.find(attrs={"class":"breadcrumb"}).find("li", class_="active").previous_sibling.previous_sibling.text.strip()
    cover = soup.find("img")['src'][6:]
    table_items = soup.find(attrs={"class":"table"}).find_all('td')
    upc = table_items[0].text
    product_type = table_items[1].text
    price_wo_tax = table_items[2].text[2:].strip()
    price_w_tax = table_items[3].text[2:].strip()
    tax = table_items[4].text[2:].strip()
    availability = only_num(table_items[5].text)
    number_of_reviews = table_items[6].text
    write_to_csv([title, price, stock, category, cover, upc, product_type, price_wo_tax, price_w_tax, tax, availability, number_of_reviews])
  i += 1

print(f'Se procesarion {line_count} libros.')