import tweepy
import time
import json
import geocoder

from urllib import urlopen
from bs4 import BeautifulSoup



import pandas as pd
pd.options.mode.chained_assignment = None

consumer_token = '33vZHXkQiOjJMdhybWEVyry2T'
consumer_secret = 'lqd1cG4Jm28xh3c8NqANvar0f8duc9eGMx1D5GbDCnOj8zu7iE'

access_token = '27821157-la768cgDthKzjwej8K2bq3ZxjILX5hXu5BZOE4R47'
access_secret = 'YiymUJfhAe2JDjyKMpKxEVSbtr20ereAbZJVqG4QyZTcF'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def getTitle(url):
    u = urlopen(url)
    title = BeautifulSoup(u, 'html.parser').title
    return title

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()


        self.tweet_file = open('tweets.json', 'a')
        self.tweetList = []
        self.fileCount = 1
        self.importantColumns = {"text": 1,
                "full_name" : 1,
                "id": 1,
                "entities": 1,
                "favorite_count": 1,
                "retweet_count": 1,
                "timestamp_ms": 1,
                "user": 1,
                "extended_text": 1,
                "created_at": 1,
                "place" : 1 }


    def on_data(self, tweet):
        #self.tweet_file.append(json.loads(tweet))
        print("===TWEET TEXT===")
        theTweet = json.loads(tweet)
        
        '''
        for key in theTweet.keys():
            if key not in self.importantColumns:
                theTweet.pop(key,None)

        titleList = []
        if len(theTweet['entities'][u'urls']) > 0:
            titleList = []
            for eachURL in theTweet['entities'][u'urls']:
                titleList.append(getTitle(eachURL[u'expanded_url']))

        theTweet['title'] = titleList

        theTweet = json.dumps(theTweet)
        self.tweetList.append(theTweet)
        if self.tweetList > 5: 
            self.tweet_file.write(theTweet)
        '''
        
        
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
                    theTweet['place'][u'bounding_box'][u'coordinates'] ]
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
                    theTweet['place'][u'bounding_box'][u'coordinates'] ]
        
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
       
            self.tweetFrame['titles'] = None

            for index, row in self.tweetFrame.iterrows():
                
                print("row url: ", row['urls'])
                if len(row['urls']) > 0:
                    
                    titleList = []
                    for eachURL in row['urls']:
                        #print("eachURL: " , eachURL)
                        #print("eachURL[u'url']: ", eachURL[u'expanded_url'])

                        title = getTitle(eachURL[u'expanded_url'])
                        print("TITLE: ", title)
                        titleList.append(title)
                    self.tweetFrame.at[index, 'titles'] = self.tweetList
            #self.tweetFrame['json'] = self.tweetFrame.apply(lambda x: x.to_json(), axis=1) 

            #self.tweetFrame.apply(lambda x: self.tweet_file.write(x['json'] + '\n'))
            self.tweetList = []
            for eachjson in self.tweetFrame.to_json(orient = 'records', lines = True):
                self.tweet_file.write(eachjson)
                
                
    


            




        #self.tweet_file.write(str(tweet))

    def on_error(self, status_code):
        if status_code == 420:
            print("ERROR: Status Code: " + status_code)
            return False
        return True

    def on_timeout(self):
        print("ERROR: Timeout")
        time.sleep(60)
        return True


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


