import tweepy
from tweepy import OAuthHandler
import auth

CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
OAUTH_TOKEN = auth.OAUTH_TOKEN
OAUTH_TOKEN_SECERT = auth.OAUTH_TOKEN_SECERT


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECERT)

api = tweepy.API(auth)

user = api.get_user('@madonna')

print(user.screen_name)
print(user.followers_count)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a tweet
    print(status.text)