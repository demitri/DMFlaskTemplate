#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

from .. import app
from . import valueFromRequest

mission_statement_page = flask.Blueprint("mission_statment_page", __name__)

@app.route('/mission-statement')
def func_name():
	''' Mission Statement page. '''
	templateDict = {}
	
	
	return render_template("mission_statement.html", **templateDict)
