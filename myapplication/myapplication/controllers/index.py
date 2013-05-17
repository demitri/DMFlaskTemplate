#!/usr/bin/python

import os

from flask import request, render_template, send_from_directory

from .. import app
from . import valueFromRequest

@app.route('/')
def func_name():
	''' Documentation here. '''
	templateDict = {}
	
	
	return render_template("index.html", **templateDict)

# This will provide the favicon for the whole site. Can be overridden for
# a single page with something like this on the page:
#    <link rel="shortcut icon" href="static/images/favicon.ico">
#
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(directory=os.path.join(app.root_path, 'static', 'images'),
                               filename='favicon.ico')#, mimetype='image/vnd.microsoft.icon')
