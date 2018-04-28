from database_functions import *
from pickle_vars import *
from send_tweet import send_tweet
import requests
import json

def add_new_posts(payload, tweet_new_posts=False):
    post_count = len(payload['posts'])
    print(post_count, "posts found")

    #loop through posts:
    for story in payload['posts']:
        author_key = story['creatorId']
        author = payload['references']['User'][author_key]
        add_story(story, author)
        if tweet_new_posts and post_count <= 5:
            added_story = get_story(story['id'])
            print(added_story)
            if not added_story[6] and not added_story[7]:
                #not sent and not excluded
                send_tweet(story['id'])
            

def fetch_posts(count=20):
    headers = {"Accept" : "application/json", 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = publication_url + 'latest/?count=' + str(count)
    result = requests.get(url, headers=headers)
    data = result.content.decode().replace('])}while(1);</x>', '')
    parsed = json.loads(data)
    
    print('fetching data from ' + url)

    if parsed['success']:
        return parsed['payload']
    else:
        return false    
