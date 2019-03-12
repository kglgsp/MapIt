## elastic search setup:
download elastic search from: https://www.elastic.co/downloads/elasticsearch
navigate to the /bin folder
run ./elasticsearch

## json loader install:
pip install elasticsearch-loader

## index the json file:
elasticsearch_loader --index incidents --type incident json tweets_array.json


## Basic Search Query:
curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/_search" -d'{"query":{"query_string":{"query":"#renovation"}}}' >> q.json

for more complicated queries see/run query.sh
