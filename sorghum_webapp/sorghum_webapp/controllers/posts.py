#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

post_grid = flask.Blueprint("post_grid", __name__)

@app.route('/posts')
def posts():
	''' List of posts '''
	templateDict = {}
	start_page = valueFromRequest(key="page", request=request) or 1
	n_per_page = valueFromRequest(key="show", request=request) or 9
	categories = valueFromRequest(key="categories", request=request)

	with wp_session(api):
		
		post_request = api.PostRequest()
		if categories:
			post_request.categories = categories
		
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = n_per_page
		post_request.page = start_page

		posts = post_request.get()
		
		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media
		
		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])
	
	print(posts)
	templateDict['posts'] = posts
	
	return render_template("posts.html", **templateDict)
