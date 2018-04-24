from setup_database import *
from twitter_connect import api

#status = api.PostUpdate("I'm working on a Python script to automatically tweet stories from the archive. This is a test Tweet.")
#print(status.text)

cursor.execute("SELECT * FROM stories ORDER BY pub_date")
for row in cursor:
    print(row[1])
