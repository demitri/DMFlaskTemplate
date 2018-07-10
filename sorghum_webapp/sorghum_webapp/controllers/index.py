#!/usr/bin/python

# This is the home page of the site.

import os
import json
import logging

import flask
import requests
from flask import send_from_directory
#from flask import request, render_template, send_from_directory
#from flask import current_app
from flask import render_template, request
import wordpress_orm as wp
from wordpress_orm import wp_session, exc
from random import randint

from . import valueFromRequest
from .. import app
from .. import wordpress_api as api
from .footer import populate_footer_template
from ..wordpress_orm_extensions.user import SBUser

#
# Note on WordPress queries. Not all information needed is returned by
# API calls. It's convenient to perform additional requests as needed
# here in the controller, but to append the data directly to records.
# To avoid stepping on any reserved words, prepend a "+" to any
# custom values added to a record.
#

#WP_BASE_URL = app.config["WP_BASE_URL"]
logger = logging.getLogger("wordpress_orm")
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
#logger.propagate = False

index_page = flask.Blueprint("index_page", __name__)

@index_page.route("/", methods=['GET'])
def index():
	'''
	Home page
	'''

	templateDict = {}

	#api = wp.API(url="http://brie6.cshl.edu/wordpress/index.php/wp-json/wp/v2/")

	# perform all WordPress requests in a single session
	with wp_session(api):

		post_request = api.PostRequest()
		post_request.categories = ["blog"]	# search by slug
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = 3			# only get three newest

		posts = post_request.get()

		small_banner = api.media(slug="sorghum-grains_1920x1000")
		templateDict["small_banner"] = small_banner
		big_banner_1 = api.media(slug="sorghum_sky_darker")
		templateDict["big_banner_1"] = big_banner_1
		big_banner_2 = api.media(slug="sorghum_close_darker")
		templateDict["big_banner_2"] = big_banner_2
		big_banner_3 = api.media(slug="sorghum_sky")
		templateDict["big_banner_3"] = big_banner_3

		photos_to_credit = [big_banner_1, big_banner_2, big_banner_3, small_banner]

		user_request = api.UserRequest()
		users = user_request.get(classobject=SBUser)

		# Way to check if WP access is authenticated - all users would be returned in that case,
		# not just the ones who have posted.
		#for u in users:
		#	logger.debug("User: {0}".format(u.s.name))

		tool_request = api.PostRequest()
		tool_request.categories = ["tools"]	# search by slug
		tools = tool_request.get()

		someUsers = []
		someTools = []

		for x in range(3):
			index = randint(0, len(users)-1)
			someUsers.append(users.pop(index))

		for x in range(min(3, len(tools))):
			index = randint(0, len(tools)-1)
			someTools.append(tools.pop(index))

		if len(posts) == 0:
			# Try to do some troubleshooting.

			# Is the 'blog' category defined?
			blog_category = None
			try:
				blog_category = api.category(slug="blog")
			except wp.exc.NoEntityFound:
				logger.debug("Expected to find the 'Blog' category (identified by the slug 'blog') but not found!")

			if blog_category is not None:
				logger.debug("The 'blog' category was found, but (maybe?) no posts are flagged with that category.")

		# fetch linked objects we know we'll need while we have this open connection
		for post in posts:
			photos_to_credit.append(post.featured_media)

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=photos_to_credit)

	#for post in posts:
	#	print(post.featured_media.s.link, post.featured_media.s.source_url)
	templateDict["team"] = someUsers
	templateDict["tools"] = someTools
	templateDict["toolicons"] = ["icon-layers", "icon-telescope", "icon-globe"]
	templateDict["posts"] = posts
	logger.debug(" ============= controller finished ============= ")
	return render_template("index.html", **templateDict, zip=zip)
