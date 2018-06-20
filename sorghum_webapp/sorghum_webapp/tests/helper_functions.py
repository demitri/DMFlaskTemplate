
import json

# =======================================
# Helper functions to work with JSON data
# =======================================

# TODO: move to a common file (conftest.py? works as fixtures? - test with search.py)

def post_json(client, url, json_dict):
	return client.post(url, data=json.dumps(json_dict), content_type='application/json')	

def json_response(response):
	''' Decode JSON data from response. '''
	return json.loads(response.data.decode('utf-8'))

