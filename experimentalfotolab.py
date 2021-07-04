from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import csv
import sys

from requests_html import HTMLSession
print('Imprimiendo productos de experimental fotolab')


baseURL = "https://experimentalfotolab.cl/"

session = HTMLSession()


def getdata(url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


for rollo in rollos:

    nombre = rollo.find('li', class_="title").text.strip()
    precio = rollo.find(
        'span', class_="woocommerce-Price-amount amount").text.replace('.', '').replace('$', '').strip()
    if(rollo.find('div', class_="outofstock-badge")):
        stock = "FALSE"
    else:
        stock = "TRUE"
