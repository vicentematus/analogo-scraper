from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import csv
import sys
print('Imprimiendo productos de experimental fotolab')


url = requests.get(
    "https://www.migo.cl/collections/rollos-y-cargas/types/rollos-blanco-y-negro").text
soup = BeautifulSoup(url, 'html.parser')

file = open('migo.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Nombre", "Precio", "Stock"])


columna = soup.find('ul', class_="row small-up-1 medium-up-2 large-up-3")
rollos = columna.find_all('li', class_="column")


for rollo in rollos:
    nombre = rollo.h4.text.strip()
    precio = rollo.find('span', class_="price").text.replace(
        '.', '').replace('$', '').strip()
    stock = "none"
    if(rollo.find('div', class_="stock-product")):
        stock = "FALSE"
    else:
        stock = "TRUE"
    writer.writerow(
        [nombre, precio, stock])
    print(nombre)
    print(precio)
    print(stock)

file.close()
