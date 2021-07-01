#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

from .. import app
#from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template

new_page = flask.Blueprint("new_page", __name__)

# Note: add to __all__ in __init__.py file
@new_page.route('/path') #, methods=['GET'])
def func_name():
	''' Documentation here. '''
    templateDict = navbar_template()
	
	
	return render_template("template.html", **templateDict)
