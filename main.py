import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json


# Authentication information
consumer_key = "JA6L1Wz94sVyAxt4i7c0ETSXk"
consumer_secret = "kuP3nA4Aeqo6CWBhJkiAMjbOWi7Z9yU3zpDwhsKTw1s7HTrmO2"
access_token = "3365047967-0HqvuP0fnd1qahNR220VmWLBU5zdVEge8VR42oQ"
access_token_secret = "c6kcl9ib7O2OmoyCsXuf1L74Qd28QsNJav4QI0za4l4GQ"

# Handles all the authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Output listener
class StdOutListener(StreamListener):

    # This handles the data received from the stream
	def on_data(self, data):
		api = tweepy.API(auth)

		tweet = json.loads(data)
		tweet_id = tweet['id']

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
