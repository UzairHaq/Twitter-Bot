import tweepy
import json

consumer_key = "JA6L1Wz94sVyAxt4i7c0ETSXk"
consumer_secret = "kuP3nA4Aeqo6CWBhJkiAMjbOWi7Z9yU3zpDwhsKTw1s7HTrmO2"
access_token = "3365047967-0HqvuP0fnd1qahNR220VmWLBU5zdVEge8VR42oQ"
access_token_secret = "c6kcl9ib7O2OmoyCsXuf1L74Qd28QsNJav4QI0za4l4GQ"

user_names = ''
user_ids = []
tweet_ids = []

class TwitterBot:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)

    def retweet(self, ids):
        for tweet_id in ids:
    	    self.api.retweet(id=tweet_id)

    def search(self, query):
        searched_tweets = self.api.search(query)

        for status in searched_tweets:
            tweet_ids.append(status._json['id'])

 
if __name__ == "__main__":
    user = TwitterBot()
    user.search("Basketball")
    user.retweet(tweet_ids)