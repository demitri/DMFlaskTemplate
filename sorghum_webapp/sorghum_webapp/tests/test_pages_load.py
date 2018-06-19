
#import pytest

# "conftest.py" is automatically called by pytest.
# Define any fixtures (i.e. resources needed for testing) there.
#
# An instance of the Flask application for testing is defined as a fixture.
#

# =======================================
# Helper functions to work with JSON data
# =======================================

def post_json(client, url, json_dict):
	return client.post(url, data=json.dumps(json_dict), content_type='application/json')	

def json_response(response):
	''' Decode JSON data from response. '''
	return json.loads(response.data.decode('utf-8'))

# ==========
# Page tests
# ==========

def test_homepage_loads(client):
	response = client.get('/')
	assert response.status_code == 200

def test_faq_page_loads(client):
	response = client.get('/faq')
	print(response)
	assert response.status_code == 200

