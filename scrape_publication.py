from setup_database import *
#gather posts from Medium
import requests
import json
print('fetching data...')
publication_url = 'https://medium.com/pickle-fork/'
url = publication_url + 'latest/?count=200'
headers = {"Accept" : "application/json", 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
data = result.content.decode().replace('])}while(1);</x>', '')
parsed = json.loads(data)

if parsed['success']:
    print('data found')
    post_count = len(parsed['payload']['posts'])
    print(post_count, "posts found")

    #loop through posts:
    for post in parsed['payload']['posts']:
        print('adding ' + post['title'])
        author_key = post['creatorId']
        author = parsed['payload']['references']['User'][author_key]
        url = publication_url + post['uniqueSlug']
        cursor.execute("INSERT OR IGNORE INTO stories (medium_id, title, url, author, author_twitter, pub_date) VALUES (?,?,?,?,?,?)" , (post['id'], post['title'], url, author['name'], author['twitterScreenName'], post['latestPublishedAt']))
else:
    print('nope')

db.commit()
