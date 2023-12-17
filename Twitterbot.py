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


"""
Functions to send the tweets.

Created by Jesús Jiménez Sánchez.
"""
import logging
from twython import Twython
from twython import TwythonError
from keys import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET_KEY, bearer_token
import tweepy

client = tweepy.Client(bearer_token, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

client.create_tweet(text = "./imagen_descargada.jpg" )
client
# client.like("1613078224539615233")

# client.retweet("1613078224539615233")

# client.create_tweet(in_reply_to_tweet_id="1613078224539615233", text = "Keep learning Simplilearners")

# for tweet in api.home_timeline():
#     print(tweet.text)

# person = client.get_user(username = "narendramodi").data.id

# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)