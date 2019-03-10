import tweepy
import time
import json
import geocoder


import pandas as pd

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


        self.tweet_file = open('tweets.json', 'a')
        self.tweetList = []

    def on_data(self, tweet):
        #self.tweet_file.append(json.loads(tweet))
        print("===TWEET TEXT===")
        theTweet = json.loads(tweet)

        try:
            importantColumns = [theTweet['text' ] ,
                    theTweet['id' ],
                    theTweet['entities'][u'urls'] ,
                    theTweet['favorite_count'], 
                    theTweet['retweet_count'],
                    theTweet['timestamp_ms'] ,
                    theTweet['user'][u'profile_image_url'], 
                    theTweet['user'][u'screen_name'], 
                    theTweet ['extended_text'] , 
                    theTweet['created_at'] , 
                    theTweet['place'][u'full_name'] , 
                    theTweet['place'][u'bounding_box'] ] 
        except KeyError:
            importantColumns = [theTweet['text' ] , 
                    theTweet['id' ], 
                    theTweet['entities'][u'urls'] , 
                    theTweet['favorite_count'], 
                    theTweet['retweet_count'], 
                    theTweet['timestamp_ms'] , 
                    theTweet['user'][u'profile_image_url'], 
                    theTweet['user'][u'screen_name'], 
                    None , 
                    theTweet['created_at'], 
                    theTweet['place'][u'full_name'] , 
                    theTweet['place'][u'bounding_box'] ] 
        
        self.tweetList.append(importantColumns)
        
        if len(self.tweetList) >= 3:
            
            self.tweetFrame = pd.DataFrame(self.tweetList,columns =  ["[text]",
                "[id]",
                "urls",
                "[favorite_count]",
                "[retweet_count]",
                "[timestamp_ms]",
                "[user][u'profile_image_url']",
                "[user][u'screen_name']",
                "[extended_text]",
                "[created_at]",
                "[place][u'full_name]",
                "[place][u'bounding_box']"]) 
       

            for index, row in self.tweetFrame.iterrows():
                print("row url: ", row['urls'])
                if len(row['urls']) > 0:
                    print("The tweet " + str(row['[id]']) + " is not null")
                    
                
            self.tweetList = []

            print("===Dataframe===")
            print(self.tweetFrame)
        #self.tweet_file.write(str(tweet))

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


