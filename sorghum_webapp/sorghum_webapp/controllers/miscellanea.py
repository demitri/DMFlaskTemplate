#!/usr/bin/python

# This file contains miscellaneous entries (e.g. robots.txt, favicon.ico).

import os

import flask
import requests
from flask import send_from_directory
from flask import current_app, render_template, request

miscellanea_page = flask.Blueprint("miscellanea _page", __name__)

# This will provide the favicon for the whole site. Can be overridden for
# a single page with something like this on the page:
#    <link rel="shortcut icon" href="static/images/favicon.ico">
#
@miscellanea_page.route('/favicon.ico')
def favicon():
	static_images_dir = directory=os.path.join(current_app.root_path, 'static', 'images')
	return send_from_directory(static_images_dir, filename='favicon.ico')#, mimetype='image/vnd.microsoft.icon')

@miscellanea_page.route('/robots.txt')
def robots():
	robots_path = os.path.join(current_app.root_path, 'static')
	return send_from_directory(robots_path, "robots.txt")
