from setup_database import *
from twitter_connect import api

#status = api.PostUpdate("I'm working on a Python script to automatically tweet stories from the archive. This is a test Tweet.")
#print(status.text)

cursor.execute("SELECT * FROM stories WHERE sent = 0 AND exclude = 0 ORDER BY pub_date LIMIT 1")

for story in cursor:
    print(story[1])
    cursor.execute("UPDATE stories SET sent=1 WHERE medium_id='" + story[0] + "'")

db.commit()
    
