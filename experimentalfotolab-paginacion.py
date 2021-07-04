from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

baseURL = "https://experimentalfotolab.cl/categoria-producto/rollos-color/"

s = HTMLSession()

paginas_color35mm = []
paginas_byn35mm = []


def getdata(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def categorias():
    return ['/categoria-producto/rollos-color/?orderby=price/', '/categoria-producto/rollos-blanco-y-negro/?orderby=price/']


def paginacion(soup):
    container = soup.find('nav', {'class': 'woocommerce-pagination'})
    if container.find('a', {'class': 'next page-numbers'}):
        url = str(soup.find('a', {'class': 'next'})['href'])
        if "rollos-color" in url:
            paginas_color35mm.append(url)
        if "rollos-blanco-y-negro" in url:
            paginas_byn35mm.append(url)
        return url
    else:
        return


for categoria in categorias():
    print("hola")


while True:
    soup = getdata(baseURL)
    url = paginacion(soup)
    print("despues de salir del ciclo esta\n")
    print(url)
    if not url:
        break
