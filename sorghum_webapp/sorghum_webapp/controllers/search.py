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

search_page = flask.Blueprint("search_page", __name__)


@app.route('/search')
def search():
    ''' search template - actual searches call /search_api '''
    templateDict = {}
    categories = valueFromRequest(key="categories", request=request, aslist=True)
    if categories == None:
        categories = ['Sorghumbase','Gramene']
    templateDict['q'] = valueFromRequest(key="q", request=request)
    with wp_session(api):
        populate_footer_template(template_dictionary=templateDict, wp_api=api)

    templateDict['categories'] = categories

    posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
    templateDict["banner_media"] = posts_banner_media
    return render_template("search.html", **templateDict)
