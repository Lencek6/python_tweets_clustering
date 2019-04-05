import sys
sys.path.insert(0, 'D:\coding\tweeter_api_test\twitter_credentials.py')
import twitter_credentials
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


class TwitterStreamer():
#class for streaming and processing live tweets
    def stream_tweets(self, filter_list):
        #this handles twitter authentication and the connection to the twitter APi
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track=filter_list)


class StdOutListener(StreamListener):
#basic listener class
    def on_data(self, data):
        try:
            print(data)
            f = open("tweets.json", "a")
            f.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    filter_list = ["beer", "ale", "stout", "brew", "brewery", "pale ale", "pub"]
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filter_list)
