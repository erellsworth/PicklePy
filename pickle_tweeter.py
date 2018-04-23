#Setup database
import sqlite3
db = sqlite3.connect("picklefork.sqlite")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS stories (medium_id, title, url)")

cursor.execute("SELECT * FROM stories")
for row in cursor:
    print(row[2])
    
#gather posts from Medium
import requests
import json
print('fetching data...')
publication_url = 'https://medium.com/pickle-fork/'
url = publication_url + 'latest/?count=3'
headers = {"Accept" : "application/json", 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = result.content.decode().replace('])}while(1);</x>', '')
parsed = json.loads(data)

if parsed['success']:
    print('it worked!')
    post_count = len(parsed['payload']['posts'])
    print(post_count, "posts found")

    #loop through posts:
    for post in parsed['payload']['posts']:
        print(post['title'])
        url = publication_url + post['uniqueSlug']
        cursor.execute("INSERT INTO stories (medium_id, title, url) VALUES (?,?,?)" , (post['id'], post['title'], url))
else:
    print('nope')

#db.commit()    






#cursor.execute("create table donuts (customer, glazed, cake, due)")
#iterator.execute("insert into donuts values ('jeff', 10, 10, 30)")
#iterator.execute("select * from donuts")
#for customer in iterator.fetchall():
#    print(customer)
#iterator.execute("insert into donuts values ('kevin', 13, 13, 60)")
#iterator.execute("select * from donuts")
#for customer in iterator.fetchall():
#    print(customer)

#https://medium.com/m/oauth/authorize?client_id=d3046f4a1dd3
#   &scope=basicProfile
#   &state={{state}}
#   &response_type=code
#   &redirect_uri={{redirectUri}}
