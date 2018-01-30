#!/usr/bin/python

# from flask import request #, make_response

from flask import request, render_template, Blueprint

from .. import app
from . import valueFromRequest

assan_admin_template = Blueprint("assan_admin_template", __name__)

# Note: add to __all__ in __init__.py file
@app.route('/admin_template')
def admin_template():
	''' Documentation here. '''
	templateDict = {}
	
	templateDict["pageTitle"] = "Admin Template"
	
	return render_template("admin/pages/template.html", **templateDict)
