import csv
from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
#performing sentiment analysis and storing it in a file(test1.csv)
# Do some version specific stuff
if sys.version[0] == '3':
 from importlib import reload

 sntTweets = csv.writer(open("sentiment.csv", "w", newline=''))
if sys.version[0] == '2':
 reload(sys)
 sys.setdefaultencoding("utf-8")
 sntTweets = csv.writer(open("sentiment.csv", "w"))
alltweets = csv.reader(open("AllOfURSumOfMe_tweets.csv", 'r'))
for row in alltweets:
 blob = TextBlob(row[1])
 print(blob.sentiment.polarity)
 if blob.sentiment.polarity > 0:
    sntTweets.writerow([row[0], blob.sentiment.polarity, "positive"])
 elif blob.sentiment.polarity < 0:
    sntTweets.writerow([row[0],blob.sentiment.polarity, "negative"])
    elif blob.sentiment.polarity == 0.0:
 sntTweets.writerow([row[0], blob.sentiment.polarity, "neutral"])
#plotting graphs