import os
from main import *

prg = './main.py'

def test_exists():
    """Revisar que exista el archivo principal."""
    assert os.path.isfile(prg)

def test_create_csv_file():
  create_csv_file()
  assert os.path.isfile(CSV_FILENAME)

def test_write_to_csv():
  write_to_csv(['temp', 'foo', 'bar'])
  from main import line_count
  assert line_count != 0

def test_get_page_1_returns_200():
  assert get_page('page-1.html') == 200

def test_get_page_bookname_returns_200():
  assert get_page('a-light-in-the-attic_1000/index.html') == 200

def test_get_page_0_returns_404():
  assert get_page('page-0.html') == 404