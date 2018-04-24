#Reset database
import sqlite3
db = sqlite3.connect("picklepy.sqlite")
cursor = db.cursor()
cursor.execute("DROP TABLE stories")
db.commit() 
