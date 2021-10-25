import requests
from bs4 import BeautifulSoup

r = requests.get('https://books.toscrape.com/catalogue/page-1.html')
soup = BeautifulSoup(r.text, 'lxml')

print(r.status_code)