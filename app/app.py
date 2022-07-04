from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import elastic_client
app = Flask(__name__)
api = Api(app)
es = elastic_client.elastic_client()
class Cities(Resource):
    def get(self):
        query='''{'query': {
                'match_all' : {}
                }
            }'''
        results = es.search(index="cities")
        return jsonify(results['hits']['hits'])
class UpdateCity(Resource):
    def put(self):
        city=request.get_json()
        es.update(index="cities", id=city['_id'], doc=city['_source'],doc_as_upsert= "true")
        result = {'success': 'true'}
        return result
class Population(Resource):
    def get(self,city_id):
        results = es.get(index="cities", id=city_id)
        return jsonify(results['_source']["population"])
class Health(Resource):
    def get(self):
        return 'OK'
api.add_resource(Cities, '/cities') #
api.add_resource(UpdateCity, '/city/')#To insert/Update a City
api.add_resource(Population, '/population/<city_id>') # To get population of any city by id
api.add_resource(Health, '/health') # HealthAPI
