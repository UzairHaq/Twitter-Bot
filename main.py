import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from config import *

import json


# Handles all the authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Output listener
class StdOutListener(StreamListener):

    # This handles the data received from the stream
	def on_data(self, data):
		api = tweepy.API(auth)

		# Serialize the incoming data
		tweet = json.loads(data)
		tweet_id = tweet['id']

		# Retweet
		# This is a template, so any changes can be made 
		api.retweet(id=tweet_id)

		return True

	# This handles any errors when receiving data
	def on_error(self, status):
		print(status)
		return True

	# This handles any timeout error
	def on_timeout(self):
		print('Timeout...')
		return True 


if __name__ == '__main__':
	listener = StdOutListener()

	stream = Stream(auth, listener)
	stream.filter(track=['raptors'])
