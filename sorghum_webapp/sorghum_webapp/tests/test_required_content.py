
#
# This suite of tests check that the CMS has objects that are required for basic display.
#

import wordpress_orm
from wordpress_orm import wp_session


def test_mission_statement(client, app, wp_api):
	'''
	Test that a post for containing the mission statement exists.
	'''
	with wp_session(wp_api):
		mission_statement_slug = 'mission-statement'
		try:
			ms_post = wp_api.post(slug=mission_statement_slug)
		except wordpress_orm.exc.NoEntityFound:
			assert FALSE, "No post with the slug '{0}' found (required for mission statement.".format(mission_statement_slug)
		assert len(ms_post.s.content) > 100 # probably not correct if less than 100 characters long