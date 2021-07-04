from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

url = "https://suranalogo.cl/pelicula-35mm"

s = HTMLSession()

peliculas_35mm_paginas = []
rollos_35mm = []
result = []


def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def proxima_pagina(soup):
    page = soup.find('div', {'class': 'category-pager'})
    paginas = page.find_all('span')
    if paginas[0].text != paginas[2].text:
        print(paginas[0].text != paginas[2])
        url = 'https://suranalogo.cl' + \
            str(page.select('div > a')[1]['href'])
        getInfo(url)
        peliculas_35mm_paginas.append(url)
        return url
    else:
        return





def getInfo(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print("entre al get info")
    rollos = soup.find_all('div', class_="col-lg-3 col-md-3 col-6")

    for rollo in rollos:
        nombre = rollo.find('div', class_="caption").h4.a.text.replace('ROLLO BLANCO Y NEGRO', '').replace(
            'ROLLO PELÍCULA', '').replace('ROLLO PELICULA FOTOGRAFICA', '').strip()
        precio = rollo.find(
            'div', class_="list-price").text.replace('$', '').replace('CLP', '').replace('.', '').strip()
        stock = "none"
        agotado = rollo.find('span', class_="status-tag")
        url = "https://suranalogo.cl" + \
            str(rollo.find('a', class_="product-image")['href'].strip())
        if(agotado):
            stock = "FALSE"
        else:
            stock = "TRUE"
        informacion = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "url": url
        }
        # print(informacion)
        rollos_35mm.append(informacion)
    return


def findOnArray(string):
    for rollo in rollos_35mm:
        if rollo['nombre'].upper().replace(" ", "").find(string.upper().replace(" ", "")) != -1:
            result.append(rollo)


while True:
    soup = getdata(url)
    url = proxima_pagina(soup)
    if not url:
        break

df = pd.DataFrame(rollos_35mm)


df.to_csv('surnanalogo-35mm.csv')

