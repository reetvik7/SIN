import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
consumer_key = 'VsrywUvlqskMAmwNZEaS5zpNp'
consumer_secret = 'YHDpaJBZgIkLlIAbT1dnS49HuLHi7Pbx3TzeWZoJvFEsdt7n7w'
access_token = '1047371015339163648-st9mpBh1c2xwvmaznr4bGhLbqvYuyP'
access_secret = '1b6WmSbYxM9MC2w3mIbVlZ6ZZ28SXBzSuhkA8m43IQyKl'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
class MyListener(StreamListener):
 def on_data(self, data):
    try:
        with open('cancer.json', 'a') as f:
            f.write(data)
            return True
    except BaseException as e:
        print("Error on_data: %s" % str(e))
    return True
 def on_error(self, status):
    print(status)
    return True
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=["cancer","suffer","chemotherapy","tumour"])