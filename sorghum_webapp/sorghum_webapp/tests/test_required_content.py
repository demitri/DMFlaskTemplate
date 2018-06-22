
#
# This suite of tests check that the CMS has objects that are required for basic display.
#

import wordpress_orm
from wordpress_orm import wp_session

def test_wordpress_connection(wp_api):
	'''
	Test that the WordPress server is running.
	'''
	post_request = wp_api.PostRequest()
	post_request.per_page = 3
	posts = post_request.get()
	assert len(posts) > 0

def test_mission_statement(wp_api):
	'''
	Test that a post for containing the mission statement exists.
	'''
	with wp_session(wp_api):
		mission_statement_slug = 'mission-statement'
		try:
			ms_post = wp_api.post(slug=mission_statement_slug)
		except wordpress_orm.exc.NoEntityFound:
			assert FALSE, "No post with the slug '{0}' found (required for mission statement).".format(mission_statement_slug)
		assert len(ms_post.s.content) > 100 # probably not correct if less than 150 characters long

def test_news_entries(wp_api):
	'''
	Test that there are new entries available.
	'''
	with wp_session(wp_api):
		post_request = wp_api.PostRequest()
		post_request.categories = ["blog"]
		post_request.per_page = 3			# only get three newest
		posts = post_request.get()
		
		assert len(posts) >= 1, "No news posts found, i.e. posts with a category (slug) of 'blog'"
