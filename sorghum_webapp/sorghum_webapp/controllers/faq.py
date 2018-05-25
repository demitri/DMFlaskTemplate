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

faq_page = flask.Blueprint("faq_page", __name__)

@app.route('/faq')
def faq():
	''' FAQ page. '''
	templateDict = {}

	with wp_session(api):

		post_request = api.PostRequest()
		post_request.categories = ["faq"]
		post_request.order = "asc"
		questionSet = post_request.get()

		faq_banner_media = api.media(slug="sorghum_combine")
		templateDict["banner_media"] = faq_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[faq_banner_media])

	templateDict['questionSet'] = questionSet


	return render_template("faq.html", **templateDict)
