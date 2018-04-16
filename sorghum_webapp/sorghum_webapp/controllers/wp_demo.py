#!/usr/bin/python

import os

import flask
import requests
from flask import send_from_directory
#from flask import request, render_template, send_from_directory
from flask import current_app, render_template, request
from . import valueFromRequest

#from . import valueFromRequest

wp_demo_page = flask.Blueprint("wp_demo_page", __name__)

@wp_demo_page.route("/wp_demo", methods=['GET'])
def wp_demo():
	''' WordPress demo page. '''
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

	return render_template("wp_demo.html", **templateDict)

