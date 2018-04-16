#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

import wordpress_orm as wp
from wordpress_orm import wp_session, exc

from .. import app
from . import valueFromRequest

WP_BASE_URL = app.config["WP_BASE_URL"]

post_page = flask.Blueprint("post_page", __name__)

@app.route('/posts/<slug>')
def posts(slug):
	''' 
	This page displays a single blog post retrieved from WordPress.
	'''
	templateDict = {}
	
	api = wp.API(url="http://brie6.cshl.edu/wordpress/index.php/wp-json/wp/v2/")

	with wp_session(api):
		# get the post based on the slug
		try:
			post = api.post(slug=slug)
		except exc.NoEntityFound:
			# TODO return top level posts page
			raise Exception("Return top level posts page, maybe with an alert of 'post not found'.")
	
	templateDict["post"] = post
	
	return render_template("post.html", **templateDict)
