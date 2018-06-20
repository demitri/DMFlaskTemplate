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

		user_request = api.UserRequest()
		users = user_request.get()

		threeUsers = []

		for x in range(3):
			index = randint(0, len(users)-1)
			threeUsers.append(users.pop(index))

		populate_footer_template(template_dictionary=templateDict, wp_api=api)

		if len(posts) == 0:
			# Try to do some troubleshooting.

			# Is the 'news' category defined?
			news_category = None
			try:
				news_category = api.category(slug="news")
			except wp.exc.NoEntityFound:
				logger.debug("Expected to find the 'News' category (identified by the slug 'news') but not found!")

			if news_category is not None:
				logger.debug("The 'news' category was found, but (maybe?) no posts are flagged with that category.")

		# fetch linked objects we know we'll need while we have this open connection
		for post in posts:
			post.featured_media

	#for post in posts:
	#	print(post.featured_media.s.link, post.featured_media.s.source_url)
	templateDict["team"] = threeUsers
	templateDict["posts"] = posts
	logger.debug(" ============= controller finished ============= ")
	return render_template("index.html", **templateDict)


#@index_page.route("/", methods=['GET'])
def index2():
	'''
	Home page
	'''

	templateDict = {}

	# retrieve top news/blog entries from WordPress
	#
	with requests.Session() as http_session:

		# Get posts in the "

		params = {
			"orderby":"date",
			"order":"desc",
			"filter[category_name]":"blog"
		}
		# "categories":"??" # 'categories' takes the category ID

		# get list of blog posts
		#url = os.path.join(app.config["WP_BASE_URL"], "posts?categories={}".format(blog_posts["id"]))
		# Ref: WordPress 'posts' API: https://developer.wordpress.org/rest-api/reference/posts/
		url = os.path.join(app.config["WP_BASE_URL"], "post") #?".format(blog_posts["id"]))
		response = http_session.get(url=url, params=params)
		posts = response.json()

		app.logger.debug("WP posts URL: {}".format(url))
		app.logger.debug(json.dumps(posts, indent=4, sort_keys=True))

		# get featured media URL
		for post in posts:
			featured_media_id = post["featured_media"]

			# Ref: WordPress 'media' API: https://developer.wordpress.org/rest-api/reference/media/
			url = os.path.join(app.config["WP_BASE_URL"], "media/{}".format(featured_media_id))
			response = http_session.get(url=url, params={"context":"embed"}) #  "embed" param retrieves fewer records
			media = response.json()

			app.logger.debug("WP media URL: {}".format(url))
			app.logger.debug(json.dumps(media, indent=4, sort_keys=True))

			# append URL tp WP 'post' record
			post["+featured_media_url"] = media["source_url"] # '/wp-content' + media["source_url"].split('wp-content')[1]

		small_banner = api.media(slug="sorghum-grains_1920x1000")
		templateDict["small_banner"] = small_banner

	templateDict["blog_posts"] = posts

	return render_template("index.html", **templateDict)
