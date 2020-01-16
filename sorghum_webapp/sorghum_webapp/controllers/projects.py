#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from ..wordpress_orm_extensions.project import ProjectRequest

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

projects_list = flask.Blueprint("projects_list", __name__)

@projects_list.route('/projects')
def projects():
	''' Projects page. '''
	templateDict = {}

	with api.Session():
		project_request = ProjectRequest(api=api)

		projects = project_request.get()

		print(projects[0].project_images)

		news_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict['projects'] = projects


	return render_template("projects.html", **templateDict)
