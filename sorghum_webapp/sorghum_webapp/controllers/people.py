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
from .navbar import navbar_template
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

people_page = flask.Blueprint("people_page", __name__)

@people_page.route('/people')
def people():
	''' People page. '''
	templateDict = navbar_template('Community')

	with wpapi.Session():

		team_request = wpapi.UserRequest()
		team_request.context = "edit"
		team_request.per_page = 50
		team_request.roles = ['team_member']
		team = team_request.get(class_object=SBUser)

		leader = [u for u in team if ("Ware" in u.s.name)]
		team = [u for u in team if not ("Ware" in u.s.name)]

		cont_request = wpapi.UserRequest()
		cont_request.context = "edit"
		cont_request.per_page = 50
		cont_request.roles = ['contributor']
		contributors = cont_request.get(class_object=SBUser)

		people_banner_media = wpapi.media(slug="sorghum_combine")
		templateDict["banner_media"] = people_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=wpapi, photos_to_credit=[people_banner_media])

	templateDict['leader'] = leader[0]
	templateDict['team'] = team
	templateDict['contributors'] = contributors

	return render_template("people.html", **templateDict)
