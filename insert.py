from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'127.0.0.1','port':9200}])
print(es)

e1={
    "first_name":"Rizwan",
    "last_name":"Ansari",
    "age": 24,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}

print(e1)

res = es.index(index='megacorp',doc_type='employee',id=2,body=e1)
print(res)


res=es.get(index='megacorp',doc_type='employee',id=2)
print (res['_source'])

