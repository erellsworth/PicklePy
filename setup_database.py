#Setup database
import sqlite3
db = sqlite3.connect("picklefork.sqlite")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS stories (medium_id, title, url)")
