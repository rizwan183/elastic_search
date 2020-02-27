from elasticsearch import Elasticsearch

elastic_search = Elasticsearch([{'host':'127.0.0.1','port':9200}])
print(elastic_search)

result=elastic_search.get(index='megacorp',doc_type='employee',id=2)
print(result)
print (result['_source'])
