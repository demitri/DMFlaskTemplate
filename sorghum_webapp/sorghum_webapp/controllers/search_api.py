#!/usr/bin/python

# from flask import request #, make_response
import requests
import flask
from flask import request, jsonify

from .. import app
from . import valueFromRequest

WP_BASE_URL = app.config["WP_BASE_URL"]

WP_CATS = ['posts', 'pages', 'users', 'resources']


@app.route('/search_api/<cat>')
def search_api(cat):
    q = valueFromRequest(key="q", request=request)
    if cat in WP_CATS:
        with requests.Session() as session:
            url = WP_BASE_URL + cat + '?context=embed&search=' + q
            response = session.get(url=url)
            dict = {}
            dict['docs'] = response.json()
            dict['count'] = response.headers['X-WP-TOTAL']
            return jsonify(dict)
    elif cat == 'genes':
        with requests.Session() as session:
            url = 'http://data.gramene.org/search?q=' + q
            response = session.get(url=url)
            return jsonify(response.json())
