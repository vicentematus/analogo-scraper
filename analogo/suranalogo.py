from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import csv
import sys
print('Imprimiendo productos de suranalogo')


url = requests.get("https://suranalogo.cl/pelicula-b/n-35mm").text
soup = BeautifulSoup(url, 'html.parser')

file = open('suranalogoproductos.csv', 'w', newline='')
writer = csv.writer(file)

writer.writerow(["Nombre", "Precio", "Stock"])


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
#     print(nombre)
#     print(precio)
#     print(agotado.value)
    writer.writerow(
        [nombre, precio, stock])


file.close()
