import sys
from publication_scraper import fetch_posts
from database_functions import *

def setup():
    create_tables()
    fetch_posts(200)

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

command_list =      '1: run setup\n'
command_list +=     '2: show next story\n'
command_list +=     '3: show all stories\n'
command_list +=     '4: Tweet story\n'
command_list +=     '5: exclude story\n'
command_list +=     '6: mark story sent\n'

print(command_list)

command_options = {1 : setup,
                2 : show_next_story,
                3: list_all_stories,
                4: tweet_story,
                5: exclude,
                6: story_sent
}

command = input("command: ")

command_options[int(command)]()
