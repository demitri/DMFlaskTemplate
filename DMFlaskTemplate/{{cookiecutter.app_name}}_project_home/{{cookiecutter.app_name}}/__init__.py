#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import sys
import socket

from flask import Flask, g

from . import jinja_filters
from . import _app_setup_utils
from .utilities.color_print import print_warning, print_error, print_info, yellow_text, green_text, red_text

# ================================================================================

def register_blueprints(app=None):
	'''
	Register the code associated with each URL paths. Manually add each new
	controller file you create here.
	'''
	from .controllers.index import index_page
	#from .controllers.controller1 import xxx

	app.register_blueprint(index_page)
	#app.register_blueprint(xxx)

# ================================================================================

# place this here so that the app can be universally called (yes, a global)
app = None

def create_app(debug=False): #, conf=dict()):
	
	global app
	app = Flask(__name__) # creates the app instance using the name of the module
	app.debug = debug

	# --------------------------------------------------
	# Read configuration files.
	# -------------------------
	# You can define a different configuration
	# file based on the host the app is running on.
	#
	# Configuration files are located in the "configuration_files" directory.
	# -----------------------------------------------------------------------
	server_config_file = None
	
	# Always load the default configuration - values that need to be overridden
	# should be contained in other configuration files (see logic below).
	default_config_file = _app_setup_utils.getConfigFile("default.cfg") # returns the file path
	app.config.from_pyfile(default_config_file) # reads values into app.config dictionary

	if app.debug:
		#
		# Look for configuration file by host name (for example, can modify to taste).
		#
		hostname = socket.gethostname()		
		if "your_host" in hostname:
			server_config_file = _app_setup_utils.getConfigFile("your_host.cfg")
		else:
			server_config_file = _app_setup_utils.getConfigFile("default.cfg") # default
		
	elif app.testing:
		#
		# Get config file when testing. Can add extra logic here to test multiple configurations,
		# e.g. a testing configuration file.
		#
		server_config_file = _app_setup_utils.getConfigFile("default.cfg") # default
		
	elif app.config["USING_UWSGI"]:
		#
		# Must be in production. Look for deployment configuration file.
		#
		try:
			import uwsgi
			# The uWSGI configuration file defines a key value pair to point
			# to a particular configuration file in this module under "configuration_files".
			# The key is 'flask_config_file', and the value is the name of the configuration
			# file.
			# NOTE: For Python 3, the value from the uwsgi.opt dict below must be decoded, e.g.
			# config_file = uwsgi.opt['flask-config-file'].decode("utf-8")
			#server_config_file = _app_setup_utils.getConfigFile(uwsgi.opt['flask-config-file'])
		except ImportError:
			print("Trying to run in production mode, but not running under uWSGI.\n"
				  "You might try running again with the '--debug' (or '-d') flag.")
			sys.exit(1)
	
		# read configuration file specified in uWSGI parameters
		# (see folder: "uwsgi_configuration_files")
		config_filename = None
		try:
			config_filename = uwsgi.opt['flask-config-file'].decode("utf-8")
		except KeyError:
			print("No Flask configuration file was found (this is ok, it's optional.)")
		if config_filename:
			server_config_file = _app_setup_utils.getConfigFile(config_filename)

		else:
			raise Exception("No configuration file loaded... not sure what mode we are running in here...")

	if server_config_file:
		print(green_text("Loading config file: "), yellow_text(server_config_file))
		app.config.from_pyfile(server_config_file)
	else:
		print(yellow_text("Warning: No server configuration file found."))	
		
	# -----------------------------
	# Perform app setup below here.
	# -----------------------------
	
	if app.debug:
		#print("{0}App '{1}' created.{2}".format('\033[92m', __name__, '\033[0m'))
		print_info("Application '{0}' created.".format(__name__))
	else:
		if app.config["USING_SENTRY"]:
			_app_setup_utils.setupSentry(app, dsn=sentryDSN)

	# Change the implementation of "decimal" to a C-based version (much! faster)
	try:
		import cdecimal
		sys.modules["decimal"] = cdecimal
	except ImportError:
		pass # not available

	if app.config["USING_SQLALCHEMY"]:

		if app.config["USING_POSTGRESQL"]:
			_app_setup_utils.setupJSONandDecimal()

			# This "with" is necessary to prevent exceptions of the form:
			#    RuntimeError: working outside of application context
			#    (i.e. the app object doesn't exist yet - being created here) (?)

			with app.app_context():
				from .model.databasePostgreSQL import db

		# Establish database connection
		#
		from .model.database import Database
		database = Database()
		database.connect(flask_app=app)

		@app.teardown_appcontext
		def shutdown_session(exception=None):
			'''
			Enable Flask to automatically remove database schema at the end of the request.
			Also removes the session at app shutdown.
			Ref: http://flask.pocoo.org/docs/patterns/sqlalchemy/
			'''
			if hasattr(g, 'my_session'): # defined in model.database.py
				g.my_session.remove()

	# Register all paths (URLs) available.
	register_blueprints(app=app)

	# Register all Jinja filters in the file.
	app.register_blueprint(jinja_filters.blueprint)

	return app
	

	
	
