import tweepy
import re

from tweepy import OAuthHandler

APIkey = "xxxx"

APIsecretkey = "xxxx"

Accesstoken = "xxxx"

Accesstokensecret = "xxxx"

authorizer = OAuthHandler(APIkey, APIsecretkey)
authorizer.set_access_token(Accesstoken, Accesstokensecret)

api = tweepy.API(authorizer ,timeout=15)

all_tweets = []

search_query = 'microsoft'

# for tweet_object in tweepy.Cursor(api.search,q=search_query+" -filter:retweets",lang='en',result_type='recent').items(200):
#     all_tweets.append(tweet_object.text)

for tweet_object in tweepy.Cursor(api.search,q=search_query+" -filter:retweets",lang='en',result_type='recent').items(200):
    all_tweets.append(tweet_object.text)

print(all_tweets)
import numpy as np
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
tweets = pd.read_csv("https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv")
#Data Preprocessing
X = tweets.iloc[:, 10].values
y = tweets.iloc[:, 1].values

processed_tweets = []

for tweet in range(0, len(X)):
    # Remove all the special characters
    processed_tweet = re.sub(r'\W', ' ', str(X[tweet]))

    # remove all single characters
    processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)

    # Remove single characters from the start
    processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet)

    # Substituting multiple spaces with single space
    processed_tweet = re.sub(r'\s+', ' ', processed_tweet, flags=re.I)

    # Removing prefixed 'b'
    processed_tweet = re.sub(r'^b\s+', '', processed_tweet)

    # Converting to Lowercase
    processed_tweet = processed_tweet.lower()

    processed_tweets.append(processed_tweet)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
X = tfidfconverter.fit_transform(processed_tweets).toarray()
#Training the Sentimental Analysis Model
from sklearn.ensemble import RandomForestClassifier
text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)
text_classifier.fit(X, y)
#Predicting Sentiment for the Scraped Tweets
for tweet in all_tweets:
    # Remove all the special characters
    processed_tweet = re.sub(r'\W', ' ', tweet)

    # remove all single characters
    processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)

    # Remove single characters from the start
    processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet)

    # Substituting multiple spaces with single space
    processed_tweet = re.sub(r'\s+', ' ', processed_tweet, flags=re.I)

    # Removing prefixed 'b'
    processed_tweet = re.sub(r'^b\s+', '', processed_tweet)

    # Converting to Lowercase
    processed_tweet = processed_tweet.lower()

    sentiment = text_classifier.predict(tfidfconverter.transform([processed_tweet]).toarray())
    print(processed_tweet, ":", sentiment)

