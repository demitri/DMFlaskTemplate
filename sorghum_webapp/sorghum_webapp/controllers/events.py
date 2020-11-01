#!/usr/bin/python

# from flask import request #, make_response
from datetime import datetime

import flask
import logging
from flask import request, render_template
from ..wordpress_orm_extensions.event import EventRequest

from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

events_page = flask.Blueprint("events_page", __name__)

spacer = " & "
@events_page.route('/events')
def events():
	''' Events page. '''
	templateDict = navbar_template('News')
	past = valueFromRequest(key="past", request=request) or False
	if type(past) is str:
		past = True
	today = datetime.now()

	with api.Session():
		event_request = EventRequest(api=api)
		event_request.per_page = 50
		events = event_request.get()
		pastEvents = []
		futureEvents = []

		for e in events:
			if (datetime.strptime(e.s.start_date, '%Y-%m-%d') < today): # Is the event in the past?
				pastEvents.append(e)
			else:
				futureEvents.append(e)

		sortedFutureEvents = sorted(futureEvents, reverse=past, key=lambda k: k.s.start_date)
		sortedPastEvents = sorted(pastEvents, reverse=True, key=lambda k: k.s.start_date)

		news_banner_media = api.media(slug="sorghum_panicle")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict["eventsDisplayed"] = sortedPastEvents if past else sortedFutureEvents
	templateDict["eventsNotDisplayed"] = sortedFutureEvents if past else sortedPastEvents

	templateDict['past'] = past

	return render_template("events.html", **templateDict)
