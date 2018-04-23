#Setup database
import sqlite3
#db = sqlite3.connect("picklefork.sqlite")
#cursor = db.cursor()
#cursor.execute("create table stories (url, glazed, cake, due)")

#gather posts from Medium
import requests
import json
url = 'https://medium.com/pickle-fork/latest/?count=300'
headers = {"Accept" : "application/json", 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = result.content.decode().replace('])}while(1);</x>', '')
parsed = json.loads(data)
print(parsed['success'])



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
