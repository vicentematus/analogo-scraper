from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = Request('https://socialblade.com/youtube/top/50/mostviewed')
request = urlopen(url).read()
page = urlopen(request).read()

soup = BeautifulSoup(page, 'html.parser')

# se define el padre ya que los divs no tienen clases
rows = soup.find('div', attrs={'style:float: right; width: 900px;'}).find_all(
    'div', recursive=False)
# recursive= False para encontrar el div hijo y no seguir buscando.


print(rows)
