
# coding: utf-8

# In[ ]:

import ConfigParser
import sys
import time

from TwitterAPI import TwitterAPI

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')

api = TwitterAPI(config.get('twitter', 'consumer_key'), config.get('twitter', 'consumer_secret'), config.get('twitter', 'access_token'), config.get('twitter', 'access_token_secret'))

print 'Authorized'


# In[ ]:

r = api.request('search/tweets', {'q':'pizza'})

for item in r.get_iterator():
    print item['user']['screen_name'], ' : ', item['text'], '\n'

