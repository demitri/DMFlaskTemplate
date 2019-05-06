#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This script is used to launch {{cookiecutter.app_name}}.

Application initialization should go here.

'''
from __future__ import division
from __future__ import print_function

import argparse

from flask import Flask

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
parser.add_argument('--host',
					help="Host to run application: use '0.0.0.0' to accept connections from any server.",
					default="127.0.0.1",
					required=False)
parser.add_argument('-r','--rules',
                    help='List registered rules.',
                    action="store_true",
                    default=False,
                    required=False)

args = parser.parse_args()

# -------------------
# Create app instance
# -------------------
from {{cookiecutter.app_name}} import create_app

app = create_app(debug=args.debug) # actually creates the Flask application instance

# ------------------------------------
# Register Flask modules (if any) here
# ------------------------------------
#app.register_module(xxx)

if __name__ == "__main__":
	'''
	This is called when this script is directly run.
	uWSGI gets the "app" object (the "callable") and runs it itself.
	'''
	# Useful for debugging - specify the command line option "-r"
	# to display the list of rules (valid URL paths) available.
	#
	# Ref: http://stackoverflow.com/questions/13317536/get-a-list-of-all-routes-defined-in-the-app
	# Ref: http://stackoverflow.com/questions/17249953/list-all-available-routes-in-flask-along-with-corresponding-functions-docstrin
	if args.rules:
		for rule in app.url_map.iter_rules():
			print("Rule: {0} calls {1} ({2})".format(rule, rule.endpoint, ",".join(rule.methods)))
	
	# TODO: Switch over to new "flask run" method.
	
	if args.debug:
		# If running on a remote host via a tunnel, not that
		# Safari blocks some high ports (e.g.port 6000)
		# Ref: http://support.apple.com/kb/TS4639
		#
		# By default, app is only available from localhost.
		# To make available from any host (caution!!),
		# pass "host='0.0.0.0'" as a parameter below.
		#
		app.run(debug=args.debug, port=args.port, host=args.host)
	else:
		app.run()

# PLACE NO CODE BELOW THIS LINE - it won't get called. "app.run" is the main event loop.

