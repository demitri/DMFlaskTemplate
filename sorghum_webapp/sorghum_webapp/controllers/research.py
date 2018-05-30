#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm.scientific_paper import ScientificPaperRequest
from ..wordpress_orm.resource_link import ResourceLinkRequest

from .. import app
from .. import wordpress_api as api
from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

research_page = flask.Blueprint("research_page", __name__)

WAY_MORE_THAN_WE_WILL_EVER_HAVE = 100
@app.route('/research')
def research():
	''' List of research papers '''
	templateDict = {}

	with wp_session(api):

		# paper_request = ResourceLinkRequest(api=api)
		paper_request = ScientificPaperRequest(api=api)

		papers = paper_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		# pre-cache these items so new HTTP connections aren't made from the template
		# for p in papers:
		# 	p.categories
		# 	p.author

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	print("Papers please:", papers)
	templateDict['papers'] = papers

	logger.debug(" ============= controller finished ============= ")

	return render_template("research.html", **templateDict)
