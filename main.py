
import json
import geocoder
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor





consumer_token = '33vZHXkQiOjJMdhybWEVyry2T'
consumer_secret = 'lqd1cG4Jm28xh3c8NqANvar0f8duc9eGMx1D5GbDCnOj8zu7iE'

access_token = '27821157-la768cgDthKzjwej8K2bq3ZxjILX5hXu5BZOE4R47'
access_secret = 'YiymUJfhAe2JDjyKMpKxEVSbtr20ereAbZJVqG4QyZTcF'



class TwitterAuthentication():

    def authenticate(self):
        auth = OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return auth

class TwitterStreamer():
  
    #fetched -> where we write our file name
    def stream_tweets(self, fetched_tweet_filename, hash_tag_list):

        listener = TwitterListener(fetched_tweet_filename)

	    #should be authenticated at this point
        auth = TwitterAuthentication().authenticate()
        stream = Stream(auth, listener)
    
	    #track -> if tweet list of any
        
        g = geocoder.ip('me')
        currentLocation = g.latlng
        LOCATIONS = [currentLocation[1]-1.5,currentLocation[0]-1.5,currentLocation[1]+1.5,currentLocation[0]+1.5]
        stream.filter(locations = LOCATIONS)

#prints received tweets to console
class TwitterListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        #take data in the data of streamed data



        try:
            print("data: ", data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
        
    def on_error(self,status):
        if status == 420:
            #return False on_data method in case rate limit occurs
            return False

        print("error: ", status)
    
    def on_status(self,status):
        #iterating through listener -> grabbing info we need
        #title, content, url, coordinates, timestamp
        print("\n\n on_status: ", status)
    
        
if __name__ == "__main__":
    	
    hash_tag_list = []
    fetched_tweets_filename = "tweets.json"
    TwitterStreamer = TwitterStreamer()
    TwitterStreamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
