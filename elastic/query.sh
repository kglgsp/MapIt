
rm q.json
curl -H "Content-Type: application/json" -XGET "http://localhost:9200/index/_search" -d \
'{
"query":{"query_string":{"query":"consistency"}}
}' >> q.json
