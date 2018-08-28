
# "conftest.py" is automatically called by pytest.
# Define any fixtures (i.e. resources needed for testing) there.
#
# An instance of the Flask application for testing is defined as a fixture ("client")
# either in conftest.py or automatically via the pytest-flask extension.
#

import json
from .helper_functions import post_json, json_response


def test_authorization(wp_api):
	'''
	Test that we have authenticated with WordPress (i.e. not just public access).
	'''
	from ..wordpress_orm_extensions.user import SBUser

	# Filtering users by "role" requires authentication.
	#
	user_request = wp_api.UserRequest()
	user_request.context = "edit"
	user_request.per_page = 50
	user_request.roles = ["team_member"]
	users = user_request.get(class_object=SBUser)

	json_response = user_request.response.json()

	assert user_request.response.status_code == 200, "Authentication failed. Server message: {0}".format(json_response["message"])
