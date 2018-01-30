#!/usr/bin/python

import os

import flask
import requests
from flask import send_from_directory
#from flask import request, render_template, send_from_directory
from flask import current_app, render_template, request
from . import valueFromRequest

#from . import valueFromRequest

index_page = flask.Blueprint("index_page", __name__)

@index_page.route("/", methods=['GET'])
def index():
	''' Index page. '''
	templateDict = {}
#	templateDict["msg"] = "hello"
#	templateDict["numbers"] = "1 2 3 4 5s"

	# get ID of 'News' category
	with requests.Session() as session:
		url = "http://brie6.cshl.edu/wordpress/index.php/wp-json/wp/v2/categories?slug=news"
		response = session.get(url=url)
		news_category = response.json()[0]

		url = "http://brie6.cshl.edu/wordpress/index.php/wp-json/wp/v2/posts?categories={}".format(news_category["id"])
		response = session.get(url=url)

		posts = response.json()

		# get featured media URL
		for post in posts:
			url = "http://brie6.cshl.edu/wordpress/index.php/wp-json/wp/v2/media/{}".format(post["featured_media"])
			response = session.get(url=url)
			post["_featured_media_url"] = response.json()["source_url"]
		
	#print(post0["slug"])
	
	#templateDict["msg"] = valueFromRequest(key="msg", request=request)

	templateDict["news_posts"] = posts

	return render_template("index.html", **templateDict)

# This will provide the favicon for the whole site. Can be overridden for
# a single page with something like this on the page:
#    <link rel="shortcut icon" href="static/images/favicon.ico">
#
@index_page.route('/favicon.ico')
def favicon():
	static_images_dir = directory=os.path.join(current_app.root_path, 'static', 'images')
	return send_from_directory(static_images_dir, filename='favicon.ico')#, mimetype='image/vnd.microsoft.icon')

@index_page.route('/robots.txt')
def robots():
	robots_path = os.path.join(current_app.root_path, 'static')
	return send_from_directory(robots_path, "robots.txt")
