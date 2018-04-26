from database_connection import *

def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS stories (medium_id UNIQUE, title, url, author, author_twitter, pub_date, sent INTEGER DEFAULT 0, exclude INTEGER DEFAULT 0)")
    db.commit()

def empty_database():
    cursor.execute("DROP TABLE stories")
    db.commit()

def list_all_stories():
    cursor.execute("SELECT * FROM stories")
    for story in cursor:
        print(story[0] + ' - ' + story[1])

def list_sent_stories():
    cursor.execute("SELECT * FROM stories WHERE sent = 1")
    for story in cursor:
        print(story[0] + ' - ' + story[1])

def list_excluded_stories():
    cursor.execute("SELECT * FROM stories WHERE exclude = 1")
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
