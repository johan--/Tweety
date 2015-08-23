
# coding: utf-8

# In[159]:

import ConfigParser
import sys
import time
import tweepy
import operator

from collections import defaultdict

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')

auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'), config.get('twitter', 'consumer_secret'))
auth.set_access_token(config.get('twitter', 'access_token'), config.get('twitter', 'access_token_secret'))

api = tweepy.API(auth)

print 'Authorized'


# In[160]:

tweets = []

screen_name = 'BarackObama'

new_tweets = api.user_timeline(screen_name = screen_name, count=200)

tweets.extend(new_tweets)

oldest_tweet = tweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest_tweet)
    tweets.extend(new_tweets)
    oldest_tweet = tweets[-1].id - 1
    
print "Found %s tweets" % (len(tweets)), 'for', screen_name


# In[162]:

hashtagDict = {}
hashtagDict = defaultdict(lambda:[])

for tweet in range(0, len(tweets)):
    if tweets[tweet].entities.get('hashtags'):
        for hashtag in range(0, len(tweets[tweet].entities.get('hashtags'))):
            hashtagDict[tweets[tweet].entities.get('hashtags')[hashtag]['text']].append(tweets[tweet].id_str)

hashtagLenght = defaultdict(int)
for hashtag, list in hashtagDict.items():
    hashtagLenght[hashtag] = len(list)

sortedHashtag = sorted(hashtagLenght.items(), key=operator.itemgetter(1), reverse = True)

for set  in sortedHashtag:
    print set[0], set[1]

