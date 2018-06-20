#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
#from wordpress_orm.entities.user import UserRequest

from wordpress_orm import wp_session
from ..wordpress_orm_extensions.user import SBUser

from .. import app
from .. import wordpress_api as wpapi
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

people_page = flask.Blueprint("people_page", __name__)

@app.route('/people')
def people():
	''' People page. '''
	templateDict = {}

	with wp_session(wpapi):

		user_request = wpapi.UserRequest()

		team = user_request.get(classobject=SBUser)

		people_banner_media = wpapi.media(slug="sorghum_combine")
		templateDict["banner_media"] = people_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=wpapi, photos_to_credit=[people_banner_media])

	templateDict['team'] = team

	return render_template("people.html", **templateDict)
