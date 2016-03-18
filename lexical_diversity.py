import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import prettytable
import auth

CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
OAUTH_TOKEN = auth.OAUTH_TOKEN
OAUTH_TOKEN_SECERT = auth.OAUTH_TOKEN_SECERT


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECERT)
api = tweepy.API(auth)

def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

def get_average_words(tweets):
    total_words = sum([ len(tweet.split()) for tweet in tweets ])
    return 1.0*total_words/len(tweets)

print "Averagewords: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" get_lexical_diversity(hashtags)