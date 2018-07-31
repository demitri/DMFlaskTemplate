#from .helper_functions import post_json, json_response

from datetime import datetime
import requests
import json

from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

# ==========
# Search tests
# ==========
url = 'https://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/scientific_paper'

def test_valid_paper_dates(client, wp_api):
	'''
	Make sure papers in database with an abstract have valid publication dates.
	'''
	paper_request = ScientificPaperRequest(api=wp_api)
	papers = paper_request.get()
	for paper in papers:
		if paper.s.abstract is not "":
			assert datetime.strptime(paper.s.publication_date, "%Y-%m-%d")

def test_wordpress_connection(wp_api):
	'''
	Test that the WordPress server is running and returns Scientific Papers.
	'''
	r = requests.get(url)
	assert r.status_code == 200

def test_paper_schema(wp_api):
	'''
	Test that the api returns the same schema as is defined in the ORM.
	'''
	r = requests.get(url)
	rl_request = ScientificPaperRequest(api=wp_api)
	rl_request.per_page = 1
	rls = rl_request.get()
	ormSchema = list(rls[0].s.__dict__)
	apiSchema = list(r.json()[0])
	apiSchema.pop() # Removes "_links" property

	assert ormSchema == apiSchema
