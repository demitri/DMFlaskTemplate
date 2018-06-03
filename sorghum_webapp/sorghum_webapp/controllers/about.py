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

about_page = flask.Blueprint("about_page", __name__)

@app.route('/about')
def about():
	''' News page. '''
	templateDict = {}

	with wp_session(api):
		ms_post = api.post(slug='mission-statement')

		post_request = api.PostRequest()
		post_request.categories = ["faq"]
		questionSet = post_request.get()

		threeQuestions = []

		for x in range(min(len(questionSet), 3)):
			index = randint(0, len(questionSet)-1)
			threeQuestions.append(questionSet.pop(index))

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['ms_post'] = ms_post
	templateDict['questionSet'] = threeQuestions

	return render_template("about.html", **templateDict)
