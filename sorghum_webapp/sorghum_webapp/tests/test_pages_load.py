
# "conftest.py" is automatically called by pytest.
# Define any fixtures (i.e. resources needed for testing) there.
#
# An instance of the Flask application for testing is defined as a fixture ("client")
# either in conftest.py or automatically via the pytest-flask extension.
#

from .helper_functions import post_json, json_response

# ==========
# Page tests
# ==========

def test_homepage_loads(client):
	response = client.get('/')
	assert response.status_code == 200

def test_faq_page_loads(client):
	response = client.get('/mission-statement')
	assert response.status_code == 200

	
