from elasticsearch import Elasticsearch
from os import environ
from elasticsearch import helpers
def elastic_client():
    ELASTIC_URL=environ.get('ELASTIC_URL')
    es = Elasticsearch(ELASTIC_URL)
    mapping = '''
    {
        "properties": {
          "city_name": {
            "type": "keyword"
          },
          "population": {
            "type": "integer"
          }
        }
      }'''
    index_name = 'cities'
    index_exists = es.indices.exists(index = index_name)
    if not index_exists:
        es.indices.create(index = index_name,mappings={
            "properties": {"field": {"type": "integer"}}
        })
        docs = [{"city_name": "city1", "population": 100}, {"city_name": "city2", "population": 200},{"city_name": "city3", "population": 300} ,{"city_name": "city4", "population": 400}]
        helpers.bulk(es, docs, index=index_name)

    return es