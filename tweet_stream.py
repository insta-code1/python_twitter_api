from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import auth

CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
OAUTH_TOKEN = auth.OAUTH_TOKEN
OAUTH_TOKEN_SECERT = auth.OAUTH_TOKEN_SECERT

keyword_list = ['python', 'java', 'c#', 'ruby'] #track list

class MyStreamListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print("Failed on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECERT)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
