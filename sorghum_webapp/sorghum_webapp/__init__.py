#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import os
import sys
import socket
import logging

import coloredlogs
import wordpress_orm
from flask import Flask

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
	from .controllers.miscellanea import miscellanea_page
	from .controllers.assan_blank import assan_blank_page
	from .controllers.admin_template import assan_admin_template
	from .controllers.notebook import notebook_page
	from .controllers.post import post_page
	from .controllers.posts import post_grid
	from .controllers.mission_statement import mission_statement_page
	from .controllers.resource_links import resource_links_page
	from .controllers.contact import contact_page
	from .controllers.people import people_page
	from .controllers.faq import faq_page
	from .controllers.search import search_page
	from .controllers.search_api import search_api
	from .controllers.publications import publications_page
	from .controllers.jobs import jobs_page
	from .controllers.mailing_list import mailing_list_page
	from .controllers.events import events_page
	from .controllers.news import news_page
	from .controllers.about import about_page
	from .controllers.community import community_page
	from .controllers.resources import resources_page
	from .controllers.projects import projects_list
	from .controllers.project import project_page
	from .controllers.clear_wp_cache import clear_wp_cache_page

	from .controllers.VEP import VEP_entry_page
	from .controllers.VEP import VEP_source_page
	from .controllers.VEP import VEP_page
	from .controllers.gramoogle import gramoogle_page
	#from .controllers.controller1 import xxx

	app.register_blueprint(index_page)
	app.register_blueprint(miscellanea_page)
	app.register_blueprint(assan_blank_page)
	app.register_blueprint(assan_admin_template)
	app.register_blueprint(post_page)
	app.register_blueprint(post_grid)
	app.register_blueprint(mission_statement_page)
	app.register_blueprint(resource_links_page)
	app.register_blueprint(contact_page)
	app.register_blueprint(people_page)
	app.register_blueprint(faq_page)
	app.register_blueprint(search_page)
	app.register_blueprint(publications_page)
	app.register_blueprint(jobs_page)
	app.register_blueprint(mailing_list_page)
	app.register_blueprint(events_page)
	app.register_blueprint(news_page)
	app.register_blueprint(about_page)
	app.register_blueprint(community_page)
	app.register_blueprint(resources_page)
	app.register_blueprint(projects_list)
	app.register_blueprint(project_page)
	app.register_blueprint(search_api)
	app.register_blueprint(clear_wp_cache_page)

	app.register_blueprint(VEP_entry_page)
	app.register_blueprint(VEP_source_page)
	app.register_blueprint(VEP_page)
	app.register_blueprint(gramoogle_page)
	#app.register_blueprint(xxx)

	if (app.debug):
		from .controllers.sandbox import sandbox_page
		app.register_blueprint(sandbox_page)

# ================================================================================

#try:
#	app
#except NameError:
#	app = Flask(__name__)

app = None

# defined here so that other files can import this object
wordpress_api = None # define below after configuration is read -> app.config["WP_BASE_URL"]

# set up wordpress-orm logger
# can be called multiple times as it's a singleton
#wordpress_orm_logger = None
#app_logger = None

def setUpLoggers(log_level="WARNING"):
	'''
	Set up loggers for this application.
	'''
	# Loggers can be called multiple times as they are implemented a singleton.
	# To access a logger from elsewhere, retrieve it by name - a new one won't be created:
	#
	# import logging
	# wp_logger = logging.getLogger("wordpress_orm")
	#

	# set up logging output format
	# ref: https://stackoverflow.com/questions/533048/how-to-log-source-file-name-and-line-number-in-python
	#
#	logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#						datefmt='%Y-%m-%d:%H:%M:%S',
#						level=logging.DEBUG)

	# coloredlogs is configured with environment variables... weird
	# define them here instead of from the shell
	# Ref: Logging attributes: https://docs.python.org/3/library/logging.html#logrecord-attributes
	#
	os.environ["COLOREDLOGS_LOG_FORMAT"] = "%(asctime)s [%(msecs)4dms] %(levelname)-8s [%(name)s] [%(filename)s:%(lineno)d] %(message)s"
	#os.environ["COLOREDLOGS_DATE_FORMAT"] = "date format here"

	color_logs = app.config.get("ENABLE_COLOR_LOGS", False)

	# ------------------------
	# application level logger
	# ------------------------
	app_logger = logging.getLogger("sorghumbase")
	console_handler = logging.StreamHandler()
	app_logger.addHandler(console_handler)
	if color_logs:
		# This adds a handler to the logger.
		#logger.setLevel(logging.DEBUG)
		coloredlogs.install(level=logging.getLevelName(log_level), logger=app_logger)
	else:
		# The code below should be used *INSTEAD* if colorless logs are prefer
		# Where should logging output go?
		#
		ch = logging.StreamHandler()  # output to console
		ch.setLevel(getattr(logging, log_level))   # set log level for output
		app_logger.addHandler(ch)         # add to logger


	# --------------------
	# wordpress_orm logger
	# --------------------
	wordpress_orm_logger = logging.getLogger("wordpress_orm")
	console_handler = logging.StreamHandler()
	wordpress_orm_logger.addHandler(console_handler)
	if color_logs:
		# This adds a handler to the logger.
		#logger.setLevel(logging.DEBUG)
		coloredlogs.install(level=logging.getLevelName(log_level), logger=wordpress_orm_logger)
	else:
		# The code below should be used *INSTEAD* if colorless logs are prefer
		# Where should logging output go?
		#
		ch = logging.StreamHandler()  # output to console
		ch.setLevel(getattr(logging, log_level))   # set log level for output
		wordpress_orm_logger.addHandler(ch)         # add to logger

def create_app(debug=False, log_level=None):#, conf=dict()):

	#print(" = = = = = = = = = = = creating app ...")

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
		# Look for configuration file by host name.
		#
		hostname = socket.gethostname()
		if "your_host" in hostname:
			server_config_file = _app_setup_utils.getConfigFile("your_host.cfg")
		else:
			server_config_file = _app_setup_utils.getConfigFile("default.cfg") # default

	elif app.testing:
		#
		# Get config file when testing. Can add extra logic here to test multiple configurations.
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
		except ImportError:
			print("Trying to run in production mode, but not running under uWSGI.\n"
				  "You might try running again with the '--debug' (or '-d') flag.")
			sys.exit(1)

		# read configuration file specified in uWSGI parameters
		config_filename = None
		try:
			config_filename = uwsgi.opt['flask-config-file'].decode("utf-8")
		except KeyError:
			print("No Flask configuration file was found (this is ok, it's optional.)")
		if config_filename:
			server_config_file = _app_setup_utils.getConfigFile(config_filename)

	else:
		raise Exception("Not sure what mode we are running in here...")

	# Load file if found, which there almost always should be (at least in production mode).
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

	# Change the implementation of "decimal" to a C-based version (much! faster).
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

	# config is defined by now
	global wordpress_api
	wordpress_api = wordpress_orm.API(url=app.config["WP_BASE_URL"])

	# Register all paths (URLs) available.
	register_blueprints(app=app)

	# Register all Jinja filters in the file.
	app.register_blueprint(jinja_filters.blueprint)

	# -------------------------------
	# Authenticate with WordPress API
	# -------------------------------

	# basic authentication
	# --------------------
	from requests.auth import HTTPBasicAuth

	# does the configuration file request basic authentication?
	if all([key in app.config for key in ['SB_WP_USERNAME', 'SB_WP_PASSWORD']]):
		# check username, password defined in local environment
		if 'SB_WP_USERNAME' not in os.environ:
			raise Exception("'SB_WP_USERNAME' (WordPress username for basic authentication) set in configuration, but not defined in local environment.")
		if 'SB_WP_PASSWORD' not in os.environ:
			raise Exception("'SB_WP_PASSWORD' (WordPress password for basic authentication) set in configuration, but not defined in local environment.")
		wordpress_api.authenticator = HTTPBasicAuth(os.environ['SB_WP_USERNAME'], os.environ['SB_WP_PASSWORD'])
	else:
		print(red_text("Basic authentication failed."))

	setUpLoggers(log_level)

	# OAuth authentication
	# --------------------
#	from flask_oauth import OAuth
#	oauth = OAuth()
#	wordpress = oauth.remote_app('wordpress',
#								 base_url="base_url",
#								 request_token_url="",
#								 access_token_url="",
#								 authorize_url="",
#								 consumer_key="",
#								 consumer_secret="")


	return app
