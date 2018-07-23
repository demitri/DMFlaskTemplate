#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest

clear_wp_cache_page = flask.Blueprint("clear_wp_cache_page", __name__)

# Note: add to __all__ in __init__.py file
@clear_wp_cache_page.route('/clear_wp_cache_page') #, methods=['GET'])
def clear_wp_cache():
	''' Documentation here. '''
	templateDict = {}
	
	api.wordpress_object_cache.initialize()
	
	return render_template("template.html", **templateDict)
