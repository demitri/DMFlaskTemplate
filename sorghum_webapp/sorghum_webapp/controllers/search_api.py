#!/usr/bin/python

# from flask import request #, make_response
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
    if cat in WP_CATS:
        with requests.Session() as session:
            url = WP_BASE_URL + cat + '?context=embed&_embed=true&search=' + q
            response = session.get(url=url)
            dict = {}
            dict['docs'] = response.json()
            dict['numFound'] = int(response.headers['X-WP-TOTAL'])
            results = jsonify(dict)
    else:
        results = jsonify(WP_CATS)
    results.headers.add('Access-Control-Allow-Origin','*')
    return results
