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

resources_page = flask.Blueprint("resources_page", __name__)

@app.route('/resources')
def resources():
	''' List of sorghum resources '''
	templateDict = {}

	with wp_session(api):
		
		gramene = {}
		gramene['resource_url'] = 'http://www.gramene.org'
		gramene['resource_blurb'] = 'This is the blurb about gramene'
		gramene['resource_name'] = 'Gramene'
		gramene['resource_image'] = 'http://brie6.cshl.edu/wordpress/wp-content/uploads/2018/05/Screen-Shot-2018-05-08-at-3.24.03-PM.png'
		gramene['categories'] = ['Uncategorized']
		resources = [gramene]
		
		resources_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = resources_banner_media
		
		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[resources_banner_media])
	
	templateDict['resources_list'] = resources
	
	
	
	
	return render_template("resources.html", **templateDict)
