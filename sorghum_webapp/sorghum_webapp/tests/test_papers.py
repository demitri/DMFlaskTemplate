#from .helper_functions import post_json, json_response

from datetime import datetime as dt
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

# ==========
# Search tests
# ==========

def test_valid_paper_dates(client, wp_api):
	'''
	Make sure papers in database have valid publication dates.
	'''
	paper_request = ScientificPaperRequest(api=api)
	papers = paper_request.get()
	for paper in papers:
		dt = datetime.strptime(value, "%Y-%m-%d")
