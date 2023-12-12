import tweepy
import pandas as pd 
from ntscraper import Nitter

def descargador_de_tweets():
    scraper =Nitter()
    tweets= scraper.get_tweets("wheretobuy", mode='hashtag', number=10)
    with open("./datos/tweets.txt", "w") as doc:
        for tweet in tweets['tweets']:
            textTweet=[tweet['text']]
            for tweets in textTweet:
                doc.write(tweets)
            doc.write("\n")



client_id="a2tWNVRlZGdjY01lYlhLX2VpbW86MTpjaQ"
client_secret="cbm6HG92m9ii9dmqVIJcAKwT5RqobIw1MWN0kDKq4YGiqwKBCr"

api_key="pbxtGZYunNIfkk1ciZo6iTWAp"
api_secret="rQ2mezk1L2Wo9WjKkTXLuy5V0rXfBpNhUf9lZjnfeyi2B4EO2j"
bearer_token= "AAAAAAAAAAAAAAAAAAAAAEiKrQEAAAAAC6zjxPIdD1N2qOJIf0K%2FQHNQhDE%3DgDqrJ3CbUjztCbVrd59wDfoiXOtfzIsT9U6R6OLswX8Dz7Jlf5"
access_token= "1731378529546235904-skJ4wAPGX8CA9M3wpFMvJomM86d1p1"
access_token_secret = "xbuXApHZHlkNp3ZeGZUwTvbiXJCOQXtIZ2igHPgczvTiO"


"""# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=api_key, consumer_secret=api_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

response = client.(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)
print(f"https://twitter.com/user/status/{response.data['id']}")"""


auth = tweepy.OAuthHandler(api_key,api_secret,access_token, access_token_secret)
auth.set_access_token(api_key,api_secret)
print(auth.username)
api = tweepy.API(auth, wait_on_rate_limit=True)

#api.)     #  .update_status("hola")

