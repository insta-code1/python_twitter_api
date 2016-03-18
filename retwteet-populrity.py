import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
import auth

CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
OAUTH_TOKEN = auth.OAUTH_TOKEN
OAUTH_TOKEN_SECERT = auth.OAUTH_TOKEN_SECERT

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECERT)
api = tweepy.API(auth)

count = 100

query = 'brazil'

#get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 # the min amount of times a status is retweeted to gain entry to our list.
                  # reset this value to suit your own tests

pop_tweets = [ status for status in results if status._json['retweet_count'] > min_retweets ]

# create a dictionary of tweet text and aassociated retweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'),tweet._json['retweet_count']) for tweet in pop_tweets])

# remove any duplicates
pop_tweets_set = set(tweets_tup)

# Sort the tuple entries in decending order
sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]
# prettyify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tup:
    table.add_row([key, val])
    table.max_width['Text'] = 50
    table.align['Text'], table.align['Retweet Count'] = '1', 'r' #align the columns
print table