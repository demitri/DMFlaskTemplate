#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template

from wordpress_orm import wp_session
from ..wordpress_orm_extensions.resource_link import ResourceLinkRequest

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

resources_page = flask.Blueprint("resources_page", __name__)

@resources_page.route('/resources')
def resources():
	''' Resources page. '''
	templateDict = {}

	with api.Session():
		rl_pr = ResourceLinkRequest(api=api)
		links = rl_pr.get()

		post_request = api.PostRequest()
		post_request.categories = ['tools', 'tutorials', 'projects']
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = 9			# only get nine newest
		TTP = post_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['resource_links'] = links
	templateDict['TTP'] = TTP


	return render_template("resources.html", **templateDict)
