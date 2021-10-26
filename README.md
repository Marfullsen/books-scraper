# BooKs ScRaPeR

## Contenidos

- [¿Qué es Books Scraper?](#about)
- [Echa un vistazo](#getting_started)
- [Uso](#usage)
- [Referencias](#refs)

## ¿Qué es Books Scraper? <a name = "about"></a>

Prueba de postulación a Tech-K, el proyecto consiste en hacer _scraping_ al sitio [books.ToScrape.com](https://books.toscrape.com/), obtener la información de mil libros y entregar un archivo CSV con los datos recopilados.

## Archivo original

El archivo de instrucciones original puede encontrarse [haciendo click aquí](./INSTRUCTIONS.md)

## Echa un vistazo <a name = "getting_started"></a>

### Requisitos Previos

- Python3
- Dependencias externas para Python3

El archivo de requisitos puede ser usado con el comando `python -m pip install -r requirements.txt`

Detalladamente, las bibliotecas a instalar son:

```
pip install requests
pip install beautifulsoup4
pip install lxml
pip install pytest
```

## Uso <a name = "usage"></a>

Al tener una conexión a internet y corroborar que el sitio se encuentre estable, bastará con ejecutar el archivo `main.py`

Cada página cuenta con 20 libros, revisar cada uno de esos libros demora alrededor de un segundo **por libro**.

```
Página 1                    
Página 2                    
Página 3                    

...                  

Página 50                   
Se procesarion 1000 libros. 
```

**Nota:** Una vez iniciado el proceso se irá rellenando el archivo CSV, en caso de problemas con la ejecución, el archivo quedará con la cantidad de datos que haya logrado procesar en aquel momento.

Las pruebas unitarias se pueden realizar con el comando `pytest -xv tests.py`

## Referencias <a name = "refs"></a>

- Documentación de BS - [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Documentación de CSV - [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
- Primer libro del siito - [https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html](https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html)
- Reading and Writing CSV Files in Python - [https://realpython.com/python-csv/](https://realpython.com/python-csv/)
- Python docs, CSV Library - [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
- Enumerate Python [https://www.geeksforgeeks.org/enumerate-in-python/](https://www.geeksforgeeks.org/enumerate-in-python/)
- Fatal bad revision GIT - [stackoverflow.com/what-does-fatal-bad-revision-mean](https://stackoverflow.com/questions/14550802/what-does-fatal-bad-revision-mean)
- Snippet encoding - [https://www.codegrepper.com/code-examples/python/csv+writerow+without+newline](https://www.codegrepper.com/code-examples/python/csv+writerow+without+newline)
- Decoding - [stackoverflow.com/how-to-decode-scrambled-character-encoding-special-character-encoding](https://stackoverflow.com/questions/8706107/how-to-decode-scrambled-character-encoding-special-character-encoding)
- Pounds Charcode problem - [https://stackoverflow.com/questions/55737316/python-selenium-text-returns-%C3%A2%E2%82%AC-instead-of-apostrophe](https://stackoverflow.com/questions/55737316/python-selenium-text-returns-%C3%A2%E2%82%AC-instead-of-apostrophe)
- Encoding - [https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters](https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters)
