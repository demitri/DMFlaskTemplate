#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from ..wordpress_orm_extensions.event import EventRequest

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

events_page = flask.Blueprint("events_page", __name__)

spacer = " & "
@events_page.route('/events')
def events():
	''' Events page. '''
	templateDict = {}
	past = valueFromRequest(key="past", request=request) or False
	if type(past) is str:
		past = True

	with wp_session(api):
		event_request = EventRequest(api=api)
		event_request.past = past

		events = event_request.get()

		news_banner_media = api.media(slug="sorghum_panicle")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict['events'] = events
	templateDict['past'] = past


	return render_template("events.html", **templateDict)
