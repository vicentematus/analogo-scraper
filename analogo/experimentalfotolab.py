from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import csv
import sys
print('Imprimiendo productos de experimental fotolab')


url = requests.get(
    "https://experimentalfotolab.cl/categoria-producto/rollos-blanco-y-negro/").text
soup = BeautifulSoup(url, 'html.parser')

file = open('experimentalfotolab.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Nombre", "Precio", "Stock"])

rollos = soup.find_all('li', class_="has-product-nav")

for rollo in rollos:

    nombre = rollo.find('li', class_="title").text.strip()
    precio = rollo.find(
        'span', class_="woocommerce-Price-amount amount").text.replace('.', '').replace('$', '').strip()
    if(rollo.find('div', class_="outofstock-badge")):
        stock = "FALSE"
    else:
        stock = "TRUE"
    writer.writerow(
        [nombre, precio, stock])


file.close()
