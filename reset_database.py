#Reset database
import sqlite3
db = sqlite3.connect("picklefork.sqlite")
cursor = db.cursor()
cursor.execute("DROP TABLE stories")
db.commit() 
