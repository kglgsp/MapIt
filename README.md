# CS172:  Information Retrieval Final Project
This project utilizes the Twitter Streaming API to collect and map geolocated tweets within 100 miles from user location.

### Team: 🐦 C://Untitled 🐦 
          Katherine Legaspi
          Kevin Frazier
          Nate Mueller

## How to run:
In order to run, ./setup must first be initiated in the terminal to obtain all relevant libraries used 

Set up for Part 1 - Twitter Stream: In order to run the stream you need to run the following command:
	python main.py

After the stream is done or the stream is kicked, a sampleTweets.json will be outputted with the tweets.

Set up for Part 2 - Elastic search setup

Set up for Part 3 - Extension: Refer to Elastic search setup. When running curl with the query, add '>> q.json' to the end of the command. This will create a json file with an output of the relevant query. 

The user can simply change the word in the command line with any word he/she wants to see in "text": field, as well as the radius of the tweet in "distance": field from the user location. Refer to the image in part 3 of Report.md for an example of the execution.

Once the q.json file has been created, run the html or javascript file using any IDE you have. For my testing, I utilized Visual Studio Code's 'Live Server' extension to run a local host. The 'Live Server' extension can be found here: https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer
This creates a simple button "Go live" on the bottom of VSC that takes you to local host in any default browser.

In my test, I created the host: http://127.0.0.1:5500/

TweetToMap.js will read in the 'q.json' file and add marker/s to the relevant tweet/s with relevant information.



## Elastic search setup:
1) download elastic search from: https://www.elastic.co/downloads/elasticsearch
2) navigate to the /bin folder
3) run 
```
./elasticsearch
```
4) Install the json loader
```
pip install elasticsearch-loader
```
5) Configure the mapping for geo_points:
-do this before indexing any data so that elastic search can read geo_points
```
curl -H "Content-Type: application/json" -XPUT "http://localhost:9200/index" -d \
'{
    "mappings": {
        "tweet": {
            "properties": {
                "coordinates": {
                    "type": "geo_point"
                }
            }
        }
    }
}'
```

6) Index the json file:
```
elasticsearch_loader --index index --type tweet json [file with your tweets]
```

7) Make a query:
The following example query will search for all tweets containing the term "bedroom" within a 200km radius of the specified coordinate. 
```
curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/index/_search" -d \
'{
    "query": {
        "bool" : {
            "must" : {
                "term":{"text": "bedroom"}
            },
            "filter" : {
                "geo_distance" : {
                    "distance" : "200km",
                    "coordinates" : {"lat":34.05998,"lon":-118.165119}
                }
            }
        }
    }
}'
```
