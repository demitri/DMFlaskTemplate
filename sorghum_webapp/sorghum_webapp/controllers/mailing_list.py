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
from mailmanclient import Client

logger = logging.getLogger("wordpress_orm")

mailing_list_page = flask.Blueprint("mailing_list_page", __name__)

@mailing_list_page.route('/mailing_list', methods=['GET','POST'])
def mailing_list():
    ''' Mailing list page. '''
    templateDict = {}

    email = valueFromRequest(key="widget-subscribe-form-email", request=request)
    if email:
        # add this email address to the mailing list
        mailmanUrl = "http://brie4.cshl.edu/mailman/subscribe/sorghum-community"
        r = requests.post(mailmanUrl, data={'email': email})
        if r.status_code == 200:
            templateDict["subscribed"] = True
        else:
            templateDict["error"] = r.reason

    with wp_session(api):
        ms_banner_media = api.media(slug="sorghum_combine")
        templateDict["banner_media"] = ms_banner_media

        logger.debug(ms_banner_media.json)
        populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[ms_banner_media])

    return render_template("mailing_list.html", **templateDict)
