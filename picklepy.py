import sys
from publication_scraper import *
from send_tweet import send_tweet
from database_functions import *

def setup():
    create_tables()
    payload = fetch_posts(200)
    if(payload):
        add_new_posts(payload)

def show_next_story():
    story = get_next_story()
    print(story)

def exclude():
    medium_id = input("id: ")
    exclude_story(medium_id)
    story = get_story(medium_id)
    print('excluding ' + story[1])

def tweet_story():
    medium_id = input("id: ")
    send_tweet(medium_id)

def story_sent():
    medium_id = input("id: ")
    mark_story_sent(medium_id)
    story = get_story(medium_id)
    print(story[1] + ' marked as sent')    

def next_story_sent():
    story = get_next_story()
    mark_story_sent(story[0])
    print(story[1] + ' marked as sent') 

def manual_add_story():
    url = input("url: ")
    add_story_by_url(url)

command_list =      '1: run setup\n'
command_list +=     '2: show next story\n'
command_list +=     '3: show all stories\n'
command_list +=     '4: Tweet story by id\n'
command_list +=     '5: Tweet next story\n'
command_list +=     '6: exclude story\n'
command_list +=     '7: mark story sent by id\n'
command_list +=     '8: mark next story sent\n'
command_list +=     '9: show sent stories\n'
command_list +=     '10: show excluded stories\n'
command_list +=     '11: add story by url\n'

print(command_list)

command_options = {
                1: setup,
                2: show_next_story,
                3: list_all_stories,
                4: tweet_story,
                5: send_tweet,
                6: exclude,
                7: story_sent,
                8: next_story_sent,
                9: list_sent_stories,
                10: list_excluded_stories,
                11: manual_add_story
}

command = input("command: ")

command_options[int(command)]()
