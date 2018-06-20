#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from random import randint

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

community_page = flask.Blueprint("community_page", __name__)

@community_page.route('/community')
def community():
	''' Community page. '''
	templateDict = {}

	with wp_session(api):
		post_request = api.PostRequest()
		post_request.categories = ["blog"]	# search by slug
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = 3			# only get three newest

		blog = post_request.get()

		user_request = api.UserRequest()
		users = user_request.get()

		someUsers = []

		for x in range(2):
			index = randint(0, len(users)-1)
			someUsers.append(users.pop(index))

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['blog'] = blog
	templateDict['team'] = someUsers

	return render_template("community.html", **templateDict)
