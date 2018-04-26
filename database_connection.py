#Setup database connection
import sqlite3
db = sqlite3.connect("picklepy.sqlite")
cursor = db.cursor()
