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

def chooseFace(wpapi,users):
    for u in users:
        if wpapi.media(slug=u.s.username) is None:
            u.imgURL = u.s.avatar_urls['96']
        else:
            media = wpapi.media(slug=u.s.username)
            u.imgURL = media.s.source_url

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
        chooseFace(wpapi,team)

#         leader = [u for u in team if ("Ware" in u.s.name)]
#         team = [u for u in team if not ("Ware" in u.s.name)]

        esc_request = wpapi.UserRequest()
        esc_request.context = "edit"
        esc_request.per_page = 50
        esc_request.roles = ['former_team_member']
        escapees = esc_request.get(class_object=SBUser)
        chooseFace(wpapi,escapees)

        cont_request = wpapi.UserRequest()
        cont_request.context = "edit"
        cont_request.per_page = 50
        cont_request.roles = ['contributor']
        contributors = cont_request.get(class_object=SBUser)

        sac_request = wpapi.UserRequest()
        sac_request.context = "edit"
        sac_request.per_page = 50
        sac_request.roles = ['sac']
        sac = sac_request.get(class_object=SBUser)
        chooseFace(wpapi,sac)

        people_banner_media = wpapi.media(slug="sorghum_combine")
        templateDict["banner_media"] = people_banner_media

        populate_footer_template(template_dictionary=templateDict, wp_api=wpapi, photos_to_credit=[people_banner_media])

#     templateDict['leader'] = leader[0]
    templateDict['team'] = team
    templateDict['contributors'] = contributors
    templateDict['sac'] = sac
    templateDict['escapees'] = escapees

    return render_template("people.html", **templateDict)
