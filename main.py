import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_token = '33vZHXkQiOjJMdhybWEVyry2T'
consumer_secret = 'lqd1cG4Jm28xh3c8NqANvar0f8duc9eGMx1D5GbDCnOj8zu7iE'

access_token = '27821157-la768cgDthKzjwej8K2bq3ZxjILX5hXu5BZOE4R47'
access_secret = 'YiymUJfhAe2JDjyKMpKxEVSbtr20ereAbZJVqG4QyZTcF'


class TwitterStreamer():
  
    #fetched -> where we write our file name
    def stream_tweets(self, fetched_tweet_filename, hash_tag_list):
        listener = StdOutListener(fetched_tweet_filename)
        auth = OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)

	#should be authenticated at this point
        stream = Stream(auth, listener)
    
	#track -> if tweet list of any 
        LOCATIONS = [103.60998,1.25752,104.03295,1.44973]
        stream.filter(locations = LOCATIONS)


#prints received tweets to console
class StdOutListener(StreamListener):
    
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
        print("error: ", status)
    '''

    def on_status(self,status):
        #iterating through listener -> grabbing info we need
        #title, content, url, coordinates, timestamp

    '''
        
if __name__ == "__main__":
    	
    hash_tag_list = []
    fetched_tweets_filename = "tweets.json"
    TwitterStreamer = TwitterStreamer()
    TwitterStreamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
