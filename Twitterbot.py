from ntscraper import Nitter
import time

def descargador_de_tweets():
    scraper =Nitter()
    tweets= scraper.get_tweets("wheretobuy", mode='hashtag', number=10)
    with open("./datos/tweets.txt", "w") as doc:
        for tweet in tweets['tweets']:
            textTweet=[tweet['text']]
            for tweets in textTweet:
                doc.write(tweets)
            doc.write("\n")

from colorama import Fore
from bs4 import BeautifulSoup
import requests
import pandas as pd

def especial():
    mensaje="Look what I found in Amazon.\nMight run Out Of stock\n#ot #amazon #aitana #OTDirecto20D  #OTGala4 #dondecomprar\n"

    with open("./tweet.txt", "r") as enlace:
        lineas = enlace.readlines()
        for website in lineas:
            try:
                #print(f"llevamos {i} enlaces posteado")
                print(website)
                HEADERS= ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'})
                resultado= requests.get(website, headers=HEADERS)
                type(resultado.content)

                soup=BeautifulSoup(resultado.content, "html.parser")

                descripcion= soup.find('span', attrs={'id':'productTitle'}).text.strip()
                
                #print(descripcion)
                
                if len(descripcion)+len(mensaje)+len(website)>280:
                    new_descripcion = descripcion[:-30]
                    if len(new_descripcion)+len(mensaje)+len(website)>280:
                        client.create_tweet(text = "Look what I found in Amazon.\n#ot #amazon #OTDirecto20D  #OTGala4 #ropa #dondecomprar\n"+ str(new_descripcion)+"\n"+website)
                        lineas.remove(website)
                        print("Posted con nueva descripcion y mensaje")
                        with open("./enlaces.txt", "w") as enlace: 
                            enlace.writelines(lineas)
                            print("Se elimino todo el contenido del docs enlaces")
                    else:
                        client.create_tweet(text = mensaje+ str(new_descripcion)+"\n"+website)
                        print("Posted con nueva descripcion")
                        lineas.remove(website)
                        with open("./enlaces.txt", "w") as enlace: 
                            enlace.writelines(lineas)
                            print("Se elimino todo el contenido del docs enlaces")

                else:
                    client.create_tweet(text = mensaje+ str(descripcion)+"\n"+website)
                    print("posted normal")
                    lineas.remove(website)
                    with open("./enlaces.txt", "w") as enlace: 
                        enlace.writelines(lineas)
                        print("Se elimino todo el contenido del docs enlaces")
                i=+1
                time.sleep(1728)
            except:
                print("Ha habido un fallo")
                with open ("./datos/linkNoUsados.txt") as linksNoUsados:
                    linksNoUsados.writelines(lineas)
                    print("Links no usados fueron escritos en ./datos/linksNoUsados")
    with open("./enlaces.txt", "w") as enlace: 
        enlace.writelines(lineas)
        print("Se elimino todo el contenido del docs enlaces")


from keys import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET_KEY, bearer_token
import tweepy

client = tweepy.Client(bearer_token, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



def main():
    mensaje="Look what I found in Amazon.\nMight run Out Of stock\n#weretobuy #Sales #amazon #Buy #gadgets\n"
    i=1
    with open("./enlaces.txt", "r") as enlace:
        lineas = enlace.readlines()
        for website in lineas:
            try:
                #print(f"llevamos {i} enlaces posteado")
                print(website)
                HEADERS= ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'})
                resultado= requests.get(website, headers=HEADERS)
                type(resultado.content)

                soup=BeautifulSoup(resultado.content, "html.parser")

                descripcion= soup.find('span', attrs={'id':'productTitle'}).text.strip()
                
                #print(descripcion)
                
                if len(descripcion)+len(mensaje)+len(website)>280:
                    new_descripcion = descripcion[:-30]
                    if len(new_descripcion)+len(mensaje)+len(website)>280:
                        client.create_tweet(text = "Look what I found in Amazon.\n#sales #wheretobuy #amazon #buy \n"+ str(new_descripcion)+"\n"+website)
                        lineas.remove(website)
                        print("Posted con nueva descripcion y mensaje")
                        with open("./enlaces.txt", "w") as enlace: 
                            enlace.writelines(lineas)
                            print("Se elimino todo el contenido del docs enlaces")
                    else:
                        client.create_tweet(text = mensaje+ str(new_descripcion)+"\n"+website)
                        print("Posted con nueva descripcion")
                        lineas.remove(website)
                        with open("./enlaces.txt", "w") as enlace: 
                            enlace.writelines(lineas)
                            print("Se elimino todo el contenido del docs enlaces")

                else:
                    client.create_tweet(text = mensaje+ str(descripcion)+"\n"+website)
                    print("posted normal")
                    lineas.remove(website)
                    with open("./enlaces.txt", "w") as enlace: 
                        enlace.writelines(lineas)
                        print("Se elimino todo el contenido del docs enlaces")
                i=+1
                time.sleep(1728)
            except:
                print("Ha habido un fallo")
                with open ("./datos/linkNoUsados.txt") as linksNoUsados:
                    linksNoUsados.writelines(lineas)
                    print("Links no usados fueron escritos en ./datos/linksNoUsados")
    with open("./enlaces.txt", "w") as enlace: 
        enlace.writelines(lineas)
        print("Se elimino todo el contenido del docs enlaces")

main()