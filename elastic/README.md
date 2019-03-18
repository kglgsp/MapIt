## elastic search setup:
download elastic search from: https://www.elastic.co/downloads/elasticsearch
navigate to the /bin folder
run ./elasticsearch

## json loader install:
pip install elasticsearch-loader

## Mapping for geo_points
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

## index the json file:
```
elasticsearch_loader --index index --type tweet json [file with your tweets]
```

## delete entire index
```
curl -X DELETE 'http://localhost:9200/_all'
```

## Basic Search Query:
```
curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/index/_search" -d'{"query":{"query_string":{"query":"relate"}}}'
```

## search for everything in english language
```
curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/index/_search" -d \
'{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "lang": "en"
        }
      }
    }
  }
}'
```

## Search everything within 200 km of (34.05998,-118.165119)
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
