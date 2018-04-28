import re
from database_connection import *
from pickle_vars import *

RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)

def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS stories (medium_id UNIQUE, title, url, author, author_twitter, pub_date, sent INTEGER DEFAULT 0, exclude INTEGER DEFAULT 0)")
    db.commit()

def empty_database():
    cursor.execute("DROP TABLE stories")
    db.commit()

def list_all_stories():
    cursor.execute("SELECT * FROM stories ORDER BY pub_date")
    for story in cursor:
        print(story[0] + ' - ' + story[1])

def list_sent_stories():
    cursor.execute("SELECT * FROM stories WHERE sent = 1 ORDER BY pub_date")
    for story in cursor:
        print(story[0] + ' - ' + story[1])

def list_excluded_stories():
    cursor.execute("SELECT * FROM stories WHERE exclude = 1 ORDER BY pub_date")
    for story in cursor:
        print(story[0] + ' - ' + story[1])

def get_next_story():
    cursor.execute("SELECT * FROM stories WHERE sent = 0 AND exclude = 0 ORDER BY pub_date LIMIT 1")
    return cursor.fetchone()

def get_story(medium_id):
    cursor.execute("SELECT * FROM stories WHERE medium_id='" + medium_id + "'")
    return cursor.fetchone()

def mark_story_sent(medium_id):
    cursor.execute("UPDATE stories SET sent=1 WHERE medium_id='" + medium_id + "'")
    db.commit()

def clear_sent_stories():
    cursor.execute("UPDATE stories SET sent=0 WHERE sent=1")
    db.commit()

def exclude_story(medium_id):
    cursor.execute("UPDATE stories SET exclude=1 WHERE medium_id='" + medium_id + "'")
    db.commit()

def include_story(medium_id):
    cursor.execute("UPDATE stories SET exclude=1 WHERE medium_id='" + medium_id + "'")
    db.commit()

def add_story(story, author):    
    title = strip_emoji(story['title'])
    post_url = publication_url + story['uniqueSlug']
    author_twitter = '';
    if 'twitterScreenName' in author:
        author_twitter = author['twitterScreenName']              
        
    print('adding', title)
    #add to database
    cursor.execute("INSERT OR IGNORE INTO stories (medium_id, title, url, author, author_twitter, pub_date) VALUES (?,?,?,?,?,?)" , (story['id'], title, post_url, author['name'], author_twitter, story['latestPublishedAt']))
    db.commit()
