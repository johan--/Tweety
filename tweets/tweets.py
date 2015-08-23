
# coding: utf-8

# In[ ]:

import ConfigParser
import sys
import time

import tweepy

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')

auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'), config.get('twitter', 'consumer_secret'))
auth.set_access_token(config.get('twitter', 'access_token'), config.get('twitter', 'access_token_secret'))

api = tweepy.API(auth)

print 'Authorized'


# In[ ]:

tweets = []

screen_name = 'chicagotribune'

new_tweets = api.user_timeline(screen_name = screen_name, count=200)

tweets.extend(new_tweets)

oldest_tweet = tweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest_tweet)
    tweets.extend(new_tweets)
    oldest_tweet = tweets[-1].id - 1
    
print "Found %s tweets." % (len(tweets))

outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

print 'done'

