#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
import os
from flask import request, render_template, jsonify
from zeep import Client

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template
logger = logging.getLogger("wordpress_orm")

feedback_page = flask.Blueprint("feedback_page", __name__)
@feedback_page.route('/feedback', methods=['GET', 'POST'])
def feedbackPage():
    if request.method == 'POST':
        j = request.json
        name = j["name"]
        email = j["email"]
        subject = j["subject"]
        content = j["content"]
        category = j["category"]
        referrer = j["referrer"]
        message = f"URL   : {referrer}\nName  : {name}\nEmail : {email}\n\n{content}"
        print("message",message)
        client = Client(app.config["MANTIS_URL"])
        issue = client.service.mc_issue_add(username=os.environ["MANTIS_USERNAME"], password=os.environ["MANTIS_PASSWORD"], issue={
            'project': {'id': 38},
            'category': category,
            'summary': f"Site Feedback: {subject}",
            'description': message
        })
        responseDict = {}
        responseDict['ticket'] = issue
        return jsonify(responseDict)
    elif request.method == 'GET':
        templateDict = navbar_template('About')
        ms_banner_media = api.media(slug="aerial_combines")
        templateDict["banner_media"] = ms_banner_media

        logger.debug(ms_banner_media.json)
        populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[ms_banner_media])
        return render_template("feedback.html", **templateDict)