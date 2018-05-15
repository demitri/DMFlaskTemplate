#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm.resource_link import ResourceLinkRequest

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

resources_page = flask.Blueprint("resources_page", __name__)

@app.route('/resources')
def resources():
	''' List of sorghum resources '''
	templateDict = {}

	with wp_session(api):
		rl_pr = ResourceLinkRequest(api=api)
		resources = rl_pr.get()
				
		resources_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = resources_banner_media
		
		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[resources_banner_media])
	
	templateDict['resources_list'] = resources
	
	return render_template("resources.html", **templateDict)
