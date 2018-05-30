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

mailing_list_page = flask.Blueprint("mailing_list_page", __name__)

@app.route('/mailing_list')
def mailing_list():
	''' Mailing list page. '''
	templateDict = {}

	# with wp_session(api):
	#
	# 	ms_post = api.post(slug='contact')
	#
	# 	ms_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
	# 	templateDict["banner_media"] = ms_banner_media
	#
	# 	logger.debug(ms_banner_media.json)
	# 	populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[ms_banner_media])
	#
	# templateDict['contact'] = ms_post


	return render_template("mailing_list.html", **templateDict)
