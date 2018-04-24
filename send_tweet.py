from setup_database import *
from twitter_connect import api

cursor.execute("SELECT * FROM stories WHERE sent = 0 AND exclude = 0 ORDER BY pub_date LIMIT 1")
#medium_id UNIQUE, title, url, author, author_twitter, pub_date, sent INTEGER DEFAULT 0, exclude INTEGER DEFAULT 0
for story in cursor:
    title = story[1]
    url = story[2]
    author = story[3]
    if story[4]:
        #use Twitter handle instead of author name
        author = '@' + story[4]

    status_update = title + ' by ' + author + ' ' + url
    status = api.PostUpdate(status_update)
    print(status_update)    
    cursor.execute("UPDATE stories SET sent=1 WHERE medium_id='" + story[0] + "'")

db.commit()
    
