#connect to Twitter API
import twitter
from twitter_vars import *
#you will need to create your own twitter_vars.py file to store your API keys

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_key)
