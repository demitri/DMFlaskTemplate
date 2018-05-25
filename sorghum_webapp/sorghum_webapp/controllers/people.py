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

people_page = flask.Blueprint("people_page", __name__)

@app.route('/people')
def people():
	''' People page. '''
	templateDict = {}

	with wp_session(api):

		user_request = api.UserRequest()
		user_request.roles = "Administrator"
		team = user_request.get()

		people_banner_media = api.media(slug="sorghum_combine")
		templateDict["banner_media"] = people_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[people_banner_media])

	# print(team[2].s.avatar_urls['24'])
	templateDict['team'] = team


	return render_template("people.html", **templateDict)
