import requests
import json
import pytest

import wordpress_orm
from wordpress_orm import wp_session

from ..wordpress_orm_extensions.job import Job, JobRequest

url = 'https://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/job'

def test_wordpress_connection(wp_api):
	'''
	Test that the WordPress server is running and returns jobs.
	'''
	r = requests.get(url)
	assert r.status_code == 200

def test_event_schema(wp_api):
	'''
	Test that the api returns the same schema for jobs as is defined in the ORM.
	'''
	r = requests.get(url)
	job_request = JobRequest(api=wp_api)
	job_request.per_page = 1
	jobs = job_request.get()
	if len(jobs) == 0:
		pytest.skip('No jobs in the CMS')
	ormSchema = list(jobs[0].s.__dict__)
	apiSchema = list(r.json()[0])
	apiSchema.pop() # Removes "_links" property

	assert ormSchema == apiSchema
