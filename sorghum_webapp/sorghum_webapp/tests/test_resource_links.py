import requests
import json

import wordpress_orm
from wordpress_orm import wp_session

from ..wordpress_orm_extensions.resource_link import ResourceLinkRequest

url = 'http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/resource-link'

def test_wordpress_connection(wp_api):
	'''
	Test that the WordPress server is running and returns Resource Links.
	'''
	r = requests.get(url)
	assert r.status_code == 200

def test_resource_link_schema(wp_api):
	'''
	Test that the api returns the same schema as is defined in the ORM.
	'''
	r = requests.get(url)
	rl_request = ResourceLinkRequest(api=wp_api)
	rl_request.per_page = 1
	rls = rl_request.get()
	ormSchema = list(rls[0].s.__dict__)
	apiSchema = list(r.json()[0])
	apiSchema.pop() # Removes "_links" property

	assert ormSchema == apiSchema
