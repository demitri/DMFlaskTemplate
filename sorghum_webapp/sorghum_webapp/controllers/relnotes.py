#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
import os
from flask import request, render_template, jsonify

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template
logger = logging.getLogger("wordpress_orm")

relnotes_page = flask.Blueprint("relnotes_page", __name__)
@relnotes_page.route('/relnotes', methods=['GET'])
def feedbackPage():
    templateDict = navbar_template('About')
    ms_banner_media = api.media(slug="aerial_combines")
    templateDict["banner_media"] = ms_banner_media

    logger.debug(ms_banner_media.json)
    populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[ms_banner_media])
    return render_template("release_notes.html", **templateDict)