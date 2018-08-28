#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm_extensions.resource_link import ResourceLinkRequest

from .. import app
from .. import wordpress_api as api
from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .footer import populate_footer_template

resource_links_page = flask.Blueprint("resource_links_page", __name__)

@resource_links_page.route('/resource_links')
def resource_links():
	''' List of sorghum resources '''
	templateDict = {}

	with api.Session():
		rl_pr = ResourceLinkRequest(api=api)
		rl_pr.per_page = 100
		resources = rl_pr.get()
		print(resources[0].resource_image.s.source_url)

		resources_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		resources_default_image = api.media(slug="sorghum-grains_1920x1000")
		templateDict["banner_media"] = resources_banner_media
		templateDict["default_image"] = resources_default_image

		populate_footer_template(template_dictionary=templateDict,
								 wp_api=api,
								 photos_to_credit=[resources_banner_media])

	templateDict['resources_list'] = resources

	wp_logger.debug(" ============= controller finished ============= ")
	return render_template("resource_links.html", **templateDict)
