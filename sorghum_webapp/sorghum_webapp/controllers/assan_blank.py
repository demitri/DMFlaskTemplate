#!/usr/bin/python

import os

import flask
import requests
from flask import send_from_directory
#from flask import request, render_template, send_from_directory
from flask import current_app, render_template, request
from . import valueFromRequest

#from . import valueFromRequest

assan_blank_page = flask.Blueprint("assan_blank_page", __name__)

@assan_blank_page.route("/assan_blank", methods=['GET'])
def index():
	''' Index page. '''
	templateDict = {}

	return render_template("assan_blank.html", **templateDict)

