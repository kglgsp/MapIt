rm q.json
curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/_search"   -d \
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
}' >> q.json
