#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

tutorials_page = flask.Blueprint("tutorials_page", __name__)

@tutorials_page.route('/tutorials')
def tutorials():
	''' Tutorials page. '''
	templateDict = navbar_template()

	with api.Session():

		post_request = api.PostRequest()
		post_request.categories = ['tutorials']
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = 9			# only get nine newest
		tutorials = post_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['tutorials'] = tutorials

	return render_template("tutorials.html", **templateDict)
