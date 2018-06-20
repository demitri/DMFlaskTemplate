#!/usr/bin/python

# from flask import request #, make_response

import json

from flask import request, render_template, Blueprint

from .. import app
from . import valueFromRequest

notebook_page = Blueprint("notebook", __name__)

# -----------------------------------------------------------------

class Sequence():
	def __init__(self):
		self.sequence = None
		self.bookmarks = []
	
	def toJSON(self):
		return json.dumps({"not yet implemented"})

# -----------------------------------------------------------------
cells = list()

# Note: add to __all__ in __init__.py file
@notebook_page.route('/notebook')
def notebook():
	''' Documentation here. '''
	templateDict = {}
	
	add_cell = valueFromRequest(key="add_cell", request=request, boolean=True)
	if add_cell:
		cells.append("a new cell")
		print("here")
		
	templateDict["pageTitle"] = "Admin Template"
	
	
	templateDict["cells"] = cells
	
	return render_template("admin/pages/notebook.html", **templateDict)
