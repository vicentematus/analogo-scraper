from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import pandas as pd
from request_html import HTMLSession
print('Imprimiendo productos de suranalogo')


url = requests.get("https://suranalogo.cl/pelicula-b/n-35mm").text
soup = BeautifulSoup(url, 'html.parser')


lista_rollos = []
rollos = soup.find_all('div', class_="col-lg-3 col-md-3 col-6")


for rollo in rollos:

    nombre = rollo.find('div', class_="caption").h4.a.text.replace('ROLLO BLANCO Y NEGRO', '').replace(
        'ROLLO PELÍCULA', '').replace('ROLLO PELICULA FOTOGRAFICA', '').strip()
    precio = rollo.find('div', class_="list-price").text.strip()
    stock = "none"
    agotado = rollo.find('span', class_="status-tag")
    if(agotado):
        stock = "FALSE"
    else:
        stock = "TRUE"

    rollo_informacion = {
        'nombre': nombre,
        'precio': precio,
        'stock': stock
    }

    lista_rollos.append(rollo_informacion)


df = pd.DataFrame(lista_rollos)
print(df.head())

df.to_csv('suranalogo-blanco-negro.csv')
