#!/usr/bin/python

# from flask import request #, make_response

from flask import request, render_template

from .. import app
from . import valueFromRequest

# Note: add to __all__ in __init__.py file
@app.route('/path')
def hello_react():
	''' Documentation here. '''
	templateDict = {}
	
	
	return render_template("hello_react.html", **templateDict)
