
# This test configuration file is automatically called by pytest.

# Run this on the command line to see what fixtures are available:
#
# % py.test --fixtures
#

import pytest

from .. import create_app

#
# Fixtures are pytest resources used for testing. Define fixtures here.
# At the very least, the application must be defined as a fixure named "app".
# A "client" fixture is defined by the pytest-flask extension.
#

@pytest.fixture
def app():
	app = create_app(debug=True)
	app.testing = True
	app.debug = True
	return app

# The commented out code below is a definition for the "client" fixture
# if the pytest-flask extension is not installed. This can be used in
# tandem with pytest-flask as long as it's not called "client".

# 
@pytest.fixture
def client(request):
	'''
	Creates an instance of our Flask application to be used for testing.
	'''
	
	#print("creating client")
	# Create a test client for this application.
	# Ref: http://flask.pocoo.org/docs/0.12/api/#flask.Flask.test_client
	#
	app = create_app(debug=True)
	app.testing = True
	test_client = app.test_client()
	
	def teardown():
		# placeholder to free any resources created/allocated
		pass
	
	request.addfinalizer(teardown)
	return test_client
