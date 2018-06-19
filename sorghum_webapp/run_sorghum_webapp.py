#!/usr/bin/env python

'''
This script is used to launch myapplication.

Application initialization should go here.

'''
import argparse
import coloredlogs

from flask import Flask

# =====================================
# Set these values for your application
# =====================================
# conf = dict()
# 
# conf["USING_SQLALCHEMY"] = False
# conf["USING_POSTGRESQL"] = False
# 
# # These options only apply when the app is served in a production mode.
# conf["USING_SENTRY"]		= False	# only for use in production mode
# conf["SENTRY_DSN"]		= "insert your Sentry DSN here, e.g. 'https://...'"
# conf["USING_UWSGI"]		= True # only applies to serving the app in a production mode


# --------------------------
# Parse command line options
# --------------------------
parser = argparse.ArgumentParser(description='Script to start the application server.')
parser.add_argument('-d','--debug',
                    help='Launch app in debug mode.',
                    action="store_true",
                    required=False)
parser.add_argument('-p','--port',
                    help='Port to use in debug mode.',
                    default=5000,
                    type=int,
                    required=False)
parser.add_argument('-r','--rules',
                    help='List registered rules.',
                    action="store_true",
                    default=False,
                    required=False)
parser.add_argument('-l','--log-level',
					help="debug log level (one of debug, info, warning, critical)",
					type=str.upper, # force value to be uppercase
					default=None,
					required=False)

args = parser.parse_args()

# -------------------
# Create app instance
# -------------------
from sorghum_webapp import create_app

# Turn on debugging by default IF 'debug' was unset AND this is the main program (i.e. not called by uWSGI),
# otherwise use what is set on command line.
debug = (__name__ == "__main__") or args.debug

app = create_app(debug=debug) #, conf=conf) # actually creates the Flask application instance

# --------------
# Set up logging
# --------------
if args.log_level:
	import logging
	logger = logging.getLogger("wordpress_orm") # package name

	color_logs = app.config.get("ENABLE_COLOR_LOGS", False)

	if color_logs:
		# This adds a handler to the logger.
		#logger.setLevel(logging.DEBUG)
		coloredlogs.install(level=logging.DEBUG, logger=logger)
	else:
		# The code below should be used *INSTEAD* if colorless logs are prefer	
		# Where should logging output go?
		#
		ch = logging.StreamHandler()  # output to console
		ch.setLevel(getattr(logging, args.log_level))   # set log level for output
		logger.addHandler(ch)         # add to logger

# -----------------------------------------
# If using SQLAlchemy, uncomment this block
# -----------------------------------------
if app.config["USING_SQLALCHEMY"]:

	# Can't create the database connection unless we've created the app
	from myapplication.model.database import db

	@app.teardown_appcontext
	def shutdown_session(exception=None):
	   ''' Enable Flask to automatically remove database sessions at the
	   	end of the request or when the application shuts down.
	   	Ref: http://flask.pocoo.org/docs/patterns/sqlalchemy/
	   '''
	   db.Session.remove()

# ------------------------------------
# Register Flask modules (if any) here
# ------------------------------------
#app.register_module(xxx)

# Useful for debugging - specify the command line option "-r"
# to display the list of rules (valid URL paths) available.
#
# Ref: http://stackoverflow.com/questions/13317536/get-a-list-of-all-routes-defined-in-the-app
# Ref: http://stackoverflow.com/questions/17249953/list-all-available-routes-in-flask-along-with-corresponding-functions-docstrin
if args.rules:
    for rule in app.url_map.iter_rules():
        print("Rule: {0} calls {1} ({2})".format(rule, rule.endpoint, ",".join(rule.methods)))

if __name__ == "__main__":
    '''
    This is called when this script is directly run.
    uWSGI gets the "app" object (the "callable") and runs it itself.
    '''
    if True:
    	
    	# compile React to static JS
    
        # If running on a remote host via a tunnel, not that
        # Safari blocks some high ports (e.g.port 6000)
        # Ref: http://support.apple.com/kb/TS4639
        app.run(debug=debug, port=args.port)
    else:
        app.run()

# PLACE NO CODE BELOW THIS LINE - it won't get called. "app.run" is the main event loop.

