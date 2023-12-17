import re
from colorama import Fore
from bs4 import BeautifulSoup
import requests
import pandas as pd
def web_scraper():
    palabas_clave=["laptop","ordenador","pc","aubriculares","moviles","camaras","relojes","apple"]
    website=f"https://www.amazon.es/s?k={palabas_clave[i]}&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
    HEADERS= ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'})
    resultado= requests.get(website, headers=HEADERS)
    type(resultado.content)

    soup=BeautifulSoup(resultado.content, "html.parser")
    #print(soup)
    frases= soup.find('span', attrs={'id':'productTitle'}).text.strip()
    url_foto=soup.find('img', attrs={'class':'a-dynamic-image'}).get('src')
    imagen=requests.get(url_foto)
    with open('./imagen_descargada.jpg','wb') as file:
        file.write(imagen.content)
    print(frases)

if __name__ == "__main__":
    web_scraper()