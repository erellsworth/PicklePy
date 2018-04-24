#Setup database
import sqlite3
db = sqlite3.connect("picklepy.sqlite")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS stories (medium_id, title, url, author, author_twitter)")
