import tweepy
from textblob import TextBlob
consumer_key = 'xxxx'
consumer_key_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('AVENGERS')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print('Positive')
    elif analysis.sentiment[0]<0:
        print('Negative')
    else:
        print('Neutral')