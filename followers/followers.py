
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

for follower in api.followers_ids('chicagotribune'):
    print api.get_user(follower).screen_name
    
print 'done'

