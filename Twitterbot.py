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

api_key="Fk9rwPeeqpXLaxaU2m47KdRCS"
api_secret="Z8AQyTX1EV0YYsQkhGrVCqFxyfWQ9TBLlGgIn9mdG9JSrjTRMR"
bearer_token= r"AAAAAAAAAAAAAAAAAAAAAEiKrQEAAAAAGrt8A5zlH9%2B%2BBZIuwjJpxSnG67M%3Dx9EAScC5yT8MNXxIE9mv3dBueMrYEIr18aekaa7N6hWTEXmUX1"
access_token= "1731378529546235904-bFrclPSxgyscCrRaia62uYbU0XvJGc"
access_token_secret = "Q6Vg5szqvtWuskT4WcCAfDe6fjp5Cftv8ztG4e4nIfMZu"


client=tweepy.Client(bearer_token,api_key, api_secret, access_token, access_token_secret)
auth =tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)


#Very important to post tweets
#client.create_tweet(text ="Do you want some good stuff")


#like posts with the weird numbres of the url
#client.like("1732772751759302771")

#retweet
#client.retweet("1732772751759302771")




