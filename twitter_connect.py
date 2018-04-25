#connect to Twitter API
#requires https://github.com/bear/python-twitter
import twitter
from twitter_vars import *
#you will need to create your own twitter_vars.py file to store your API keys

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)
