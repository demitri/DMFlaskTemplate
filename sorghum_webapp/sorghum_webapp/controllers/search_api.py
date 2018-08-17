#!/usr/bin/python

# from flask import request #, make_response
import os
import requests
import flask
from flask import request, jsonify

from .. import app
from . import valueFromRequest

WP_BASE_URL = app.config["WP_BASE_URL"]

WP_CATS = ['posts', 'pages', 'users', 'resource-link', 'job', 'event', 'scientific_paper']

search_api = flask.Blueprint("search_api", __name__)

@search_api.route('/search_api/<cat>')
def searchapi(cat):
    q = valueFromRequest(key="q", request=request)
    rows = valueFromRequest(key="rows", request=request)
    if cat in WP_CATS:
        with requests.Session() as session:
            url = WP_BASE_URL + cat + '?_embed=true&search=' + q
            if cat == 'posts':
                url = url + '&categories_exclude=8,17'
            if rows:
                url = url + '&per_page=' + rows
            if cat == 'users':
                session.auth = (os.environ['SB_WP_USERNAME'], os.environ['SB_WP_PASSWORD'])
                url = WP_BASE_URL + cat + '?context=edit&roles=team_member&per_page=50&search=' + q
            response = session.get(url=url)
            dict = {}
            dict['docs'] = response.json()
            dict['numFound'] = int(response.headers['X-WP-TOTAL'])
            results = jsonify(dict)
    else:
        results = jsonify(WP_CATS)
    results.headers.add('Access-Control-Allow-Origin','*')
    return results
