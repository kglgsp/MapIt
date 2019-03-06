import tweepy
import time
import json
import geocoder
consumer_token = '33vZHXkQiOjJMdhybWEVyry2T'
consumer_secret = 'lqd1cG4Jm28xh3c8NqANvar0f8duc9eGMx1D5GbDCnOj8zu7iE'

access_token = '27821157-la768cgDthKzjwej8K2bq3ZxjILX5hXu5BZOE4R47'
access_secret = 'YiymUJfhAe2JDjyKMpKxEVSbtr20ereAbZJVqG4QyZTcF'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        tweet = []
        self.tweet_file = open('tweets.json', 'a')

    def on_data(self, tweet):
        #self.tweet_file.append(json.loads(tweet))
        print(tweet)
        self.tweet_file.write(str(tweet))

    def on_error(self, status_code):
        if status == 420:
            return False
        print("ERROR STATUS CODE: " + status_code)
        return True

    def on_timeout(self):
        print("ERROR TIMEOUT")
        time.sleep(60)
        return True

    #def on_status(self, status):


# filter by geolocation


def main():
    

    g = geocoder.ip('me')
    currentLocation = g.latlng
    LOCATIONS = [currentLocation[1]-1.5,currentLocation[0]-1.5,currentLocation[1]+1.5,currentLocation[0]+1.5]

    stream_listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
    stream = tweepy.Stream(auth=auth, listener=stream_listener)
    stream.filter(locations=LOCATIONS)

    return 0

if __name__ == "__main__":
    main()


