# TODO:

# write a test that compares the expected resource links schema (as defined in class) with what is retruned by API.
# repeat tor all custom WP types.
import requests
import json

import wordpress_orm
from wordpress_orm import wp_session

from ..wordpress_orm_extensions.event import EventRequest

url = 'https://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/event'

def test_wordpress_connection(wp_api):
	'''
	Test that the WordPress server is running and returns events.
	'''
	r = requests.get(url)
	assert r.status_code == 200

def test_event_schema(wp_api):
	'''
	Test that the api returns the same schema for events as is defined in the ORM.
	'''
	r = requests.get(url)
	event_request = EventRequest(api=wp_api)
	event_request.per_page = 2
	events = event_request.get()
	ormSchema = list(events[0].s.__dict__)
	apiSchema = list(r.json()[0])
	apiSchema.pop() # Removes "_links" property

	assert ormSchema == apiSchema
