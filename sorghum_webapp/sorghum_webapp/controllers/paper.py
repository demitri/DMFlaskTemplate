#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

import wordpress_orm as wp
from wordpress_orm import wp_session, exc
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template

WP_BASE_URL = app.config["WP_BASE_URL"]

paper_page = flask.Blueprint("paper_page", __name__)

@paper_page.route('/paper/<slug>')
def paper(slug):
	'''
	This page displays a single research paper retrieved from WordPress.
	'''
	templateDict = navbar_template()

	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")

	with api.Session():
		# get the post based on the slug
		paper_request = ScientificPaperRequest(api=api)
		paper_request.slug = slug
		requestResult = paper_request.get()

		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")

		populate_footer_template(wp_api=api, template_dictionary=templateDict, photos_to_credit=[])


	templateDict["paper"] = requestResult[0]

	templateDict["banner_media"] = sorghum_grains_image
  
	#logger.debug(" ============= controller finished ============= ")
	return render_template("paper.html", **templateDict)
