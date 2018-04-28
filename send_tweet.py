from database_functions import *
from twitter_connect import api

def send_tweet(medium_id=0):
    if(medium_id):
        story = get_story(medium_id)
    else:
        story = get_next_story()
        
    title = story[1]
    url = story[2]
    author = story[3]

    if story[4]:
        #use Twitter handle instead of author name
        author = '@' + story[4]

    status_update = '"' + title + '"\n by ' + author + '\n ' + url
    #status = api.PostUpdate(status_update)
    mark_story_sent(story[0])
    print(status_update)
