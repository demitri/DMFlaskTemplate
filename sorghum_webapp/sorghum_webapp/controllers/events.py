#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from ..wordpress_orm.event import EventRequest

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

events_page = flask.Blueprint("events_page", __name__)

@app.route('/events')
def events():
	''' Events page. '''
	templateDict = {}

	with wp_session(api):
		event_request = EventRequest(api=api)
		event_request.orderby = "start_date"

		events = event_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	print(events[0].s.featured_image)
	templateDict['events'] = events


	return render_template("events.html", **templateDict)
