
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

# Test "About" section

def test_mission_statement_page_loads(client):
	response = client.get('/mission-statement')
	assert response.status_code == 200

def faq_statement_page_loads(client):
	response = client.get('/faq')
	assert response.status_code == 200

def test_contact_page_loads(client):
	response = client.get('/contact')
	assert response.status_code == 200

# Test "News" section

def test_news_page_loads(client):
	response = client.get('/posts?categories=news')
	assert response.status_code == 200

def test_research_page_loads(client):
	response = client.get('/research')
	assert response.status_code == 200

def test_events_page_loads(client):
	response = client.get('/events')
	assert response.status_code == 200

def test_jobs_page_loads(client):
	response = client.get('/jobs')
	assert response.status_code == 200

# Test "Community" section

def test_blog_page_loads(client):
	response = client.get('/posts?categories=blog')
	assert response.status_code == 200

def test_people_page_loads(client):
	response = client.get('/people')
	assert response.status_code == 200

def test_mailing_list_page_loads(client):
	response = client.get('/mailing_list')
	assert response.status_code == 200

# Test "Resources" section

def test_resource_links_page_loads(client):
	response = client.get('/resource_links')
	assert response.status_code == 200

def test_tools_page_loads(client):
	response = client.get('/posts?categories=tools')
	assert response.status_code == 200

def test_tutorials_page_loads(client):
	response = client.get('/posts?categories=tutorials')
	assert response.status_code == 200

def test_projects_page_loads(client):
	response = client.get('/posts?categories=projects')
	assert response.status_code == 200
