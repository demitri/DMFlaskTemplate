#!/usr/bin/python

# from flask import request #, make_response
import logging

import flask
from flask import request, render_template
from wordpress_orm import wp_session

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest

from ..wordpress_orm.resource_link import ResourceLink
from ..wordpress_orm.resource_link import ResourceLinkRequest

logger = logging.getLogger("wordpress_orm")

sandbox_page = flask.Blueprint("sandbox_page", __name__)

# Note: add to __all__ in __init__.py file
@app.route('/sandbox') #, methods=['GET'])
def sandbox():
	''' A web page for experimentation and testing that will not appear in deployment. '''
	templateDict = {}
	
	with wp_session(api):
		rl_pr = ResourceLinkRequest(api=api)
		rl_pr.slugs.append("gramene")
		links = rl_pr.get()
	
	logger.debug(links)
	
	return render_template("sandbox.html", **templateDict)
