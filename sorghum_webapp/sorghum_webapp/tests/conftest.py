
# This test configuration file is automatically called by pytest.

# Run this on the command line to see what fixtures are available:
#
# % py.test --fixtures
#

import os
import pytest
import wordpress_orm

from .. import create_app

#
# Fixtures are pytest resources used for testing. Define fixtures here.
# At the very least, the application must be defined as a fixure named "app".
# A "client" fixture is defined by the pytest-flask extension.
#
# A test function can access a fixture when you provide the fixture name in
# the test function argument list, e.g. `def test_thing(app)`.
#
# Fixture scopes can be one of: "function" (default), "class", "module", "session".
# Ref: https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session
#
# function - one fixture is created for each test function
# class    - one fixture is created for each Python test class (if tests are defined that way)
# module   - one fixture is created for each module (i.e. test_*py file)
# session  - one fixture is reused over the entire test session over all tests

@pytest.fixture(scope="session")
def app():
	'''
	An instance of the Flask application used for testing.
	'''
	app = create_app(debug=True)
	app.testing = True
	app.debug = True
	return app

@pytest.fixture(scope="session")
def client(request, app):
	'''
	An instance of a client that calls the Flask application during testing.
	
	This function is a definition for the "client" fixture, i.e. a client that calls the Flask app.
	If the pytest-flask extension is used, comment out this function. This can be used in
	tandem with pytest-flask if you want as long as it's not called "client".
	'''
	
	#print("creating client")
	# Create a test client for this application.
	# Ref: http://flask.pocoo.org/docs/0.12/api/#flask.Flask.test_client
	#
	test_client = app.test_client()
	
	def teardown():
		# placeholder to free any resources created/allocated
		pass
	request.addfinalizer(teardown)

	return test_client

@pytest.fixture(scope="session") # , params=["wp_server_dev", "wp_server_prod"]) # repeat tests for each server
def wp_api(request, app):
	'''
	A reusable wordpress_orm.API object for testing.
	'''
	from requests.auth import HTTPBasicAuth
	
	# Read parameters from "request.param". If more than one
	# parameter is provided, more than one fixture is created
	# and the tests repeated with it.
	# There is no need to iterate over the parameters in this code.
	# Ref: https://docs.pytest.org/en/2.8.7/fixture.html#parametrizing-a-fixture
	
	# if request.param == "wp_server_dev":
	#	return wordpress_orm.API(url= <WP dev URL>)
	# elif request.param == "wp.server_prod":
	#	return wordpress_orm.API(url= <WP prod URL>)
	
	wordpress_api = wordpress_orm.API(url=app.config["WP_BASE_URL"])
	wordpress_api.authenticator = HTTPBasicAuth(os.environ['SB_WP_USERNAME'], os.environ['SB_WP_PASSWORD'])
	return wordpress_api
	





