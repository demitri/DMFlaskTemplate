#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm.resource_link import ResourceLinkRequest

from .. import app
from .. import wordpress_api as api
from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .footer import populate_footer_template

resource_links_page = flask.Blueprint("resource_links_page", __name__)

@app.route('/resource_links')
def resource_links():
	''' List of sorghum resources '''
	templateDict = {}

	with wp_session(api):
		rl_pr = ResourceLinkRequest(api=api)
		resources = rl_pr.get()
				
		resources_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = resources_banner_media
		
		populate_footer_template(template_dictionary=templateDict,
								 wp_api=api,
								 photos_to_credit=[resources_banner_media])
	
	templateDict['resources_list'] = resources
	
	wp_logger.debug(" ============= controller finished ============= ")
	return render_template("resource_links.html", **templateDict)
