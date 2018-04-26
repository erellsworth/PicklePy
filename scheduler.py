from send_tweet import send_tweet

#requires https://github.com/dbader/schedule
import schedule
import time

tweet_times = ["06:30", "09:30", "14:30", "18:30"]

for tweet_time in tweet_times:
    schedule.every().day.at(tweet_time).do(send_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
