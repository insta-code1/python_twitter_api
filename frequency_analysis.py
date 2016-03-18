import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
import auth


CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
OAUTH_TOKEN = auth.OAUTH_TOKEN
OAUTH_TOKEN_SECERT = auth.OAUTH_TOKEN_SECERT


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECERT)
api = tweepy.API(auth)

count = 500

query = 'love'

#Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'].encode('utf-8') for status in results]

screen_names = [status._json['user']['screen_name'].encode('utf-8') for status in results for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text'].encode('utf-8') for status in results for hashtag in status._json['entities']['hashtags']]

words = [w for t in status_texts for w in t.split()]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10]
    print

def get_lexical_diversity(items):
    if len(items) == 0:
        return "lexical diversity is null"
    else:
        return 1.0 * len(set(items)) / len(items)

def get_average_words(tweets):
    total_words = sum([ len(tweet.split()) for tweet in tweets ])
    return 1.0*total_words/len(tweets)

print "Averagewords: %s" % get_average_words(status_texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)