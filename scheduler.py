from send_tweet import send_tweet
from publication_scraper import *

#requires https://github.com/dbader/schedule
import schedule
import time

def fetch_new_posts():
    payload = fetch_posts(5)
    if(payload):
        add_new_posts(payload, True)

tweet_times = ["06:30", "09:30", "12:30", "16:30", "19:30"]

for tweet_time in tweet_times:
    schedule.every().day.at(tweet_time).do(send_tweet)

schedule.every(10).minutes.do(fetch_new_posts)

while True:
    schedule.run_pending()
    time.sleep(1)

