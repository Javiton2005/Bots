import re
from colorama import Fore
from bs4 import BeautifulSoup
import requests
import pandas as pd

website="https://www.amazon.es/Acer-Chromebook-314-CB314-2H-K8MM-Ordenador/dp/B0C8B13C5D/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=laptop&sr=8-5"
HEADERS= ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'})
resultado= requests.get(website, headers=HEADERS)
type(resultado.content)

soup=BeautifulSoup(resultado.content, "html.parser")
#print(soup)
frases= soup.find('span', attrs={'id':'productTitle'}).text.strip()
url_foto=soup.find('img', attrs={'class':'a-dynamic-image'}).get('src')
imagen=requests.get(url_foto)
with open('./imagen_descargada','wb') as file:
    file.write(imagen.content)
print(url_foto)