from datetime import datetime

def insert_es_index(es_client):
    doc = {
        'author': 'author_name',
        'text': 'Interensting content...',
        'timestamp': datetime.now(),
    }
    # resp = es_client.index(index = "test-index", id = 1, document = doc)
    resp = es_client.index(index = "test-index", document = doc)
    print(resp['result'])

def queryAll(es_client, es_index):
    print("==============={}=================".format(es_index))
    resp = es_client.search(index = es_index, query={"match_all": {}})
    print("Got %d Hits:" % resp['hits']['total']['value'])
    for hit in resp['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])