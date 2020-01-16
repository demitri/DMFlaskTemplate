#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

from .. import app
#from .. import wordpress_api as api
from . import valueFromRequest

gramoogle_page = flask.Blueprint("gramoogle_page", __name__)

# Note: add to __all__ in __init__.py file
@gramoogle_page.route('/genes') #, methods=['GET'])
def func_name():
	''' Documentation here. '''
	templateDict = {}
	
	
	return render_template("genes.html", **templateDict)
