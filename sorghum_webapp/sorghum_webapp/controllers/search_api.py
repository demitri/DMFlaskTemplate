#!/usr/bin/python

# from flask import request #, make_response
import requests
import flask
from flask import request, jsonify

from .. import app
from . import valueFromRequest

WP_BASE_URL = app.config["WP_BASE_URL"]

WP_CATS = ['posts', 'pages', 'users', 'resource-link', 'job', 'event', 'scientific_paper']

@app.route('/search_api/<cat>')
def search_api(cat):
    q = valueFromRequest(key="q", request=request)
    if cat in WP_CATS:
        with requests.Session() as session:
            url = WP_BASE_URL + cat + '?context=embed&search=' + q
            response = session.get(url=url)
            dict = {}
            dict['docs'] = response.json()
            dict['numFound'] = int(response.headers['X-WP-TOTAL'])
            results = jsonify(dict)
    elif cat == 'Sorghumbase':
        with requests.Session() as session:
            dict = {}
            dict['numFound'] = 0
            dict['categories'] = {}
            for cat in WP_CATS:
                url = WP_BASE_URL + cat + '?context=embed&_embed=true&search=' + q
                response = session.get(url=url)
                dict['numFound'] += int(response.headers['X-WP-TOTAL'])
                dict['categories'][cat] = {}
                dict['categories'][cat]['numFound'] = int(response.headers['X-WP-TOTAL'])
                dict['categories'][cat]['docs'] = response.json();
            results = jsonify(dict)
    elif cat == 'Gramene':
        with requests.Session() as session:
            url = 'http://data.gramene.org/search?q=' + q
            response = session.get(url=url)
            results = jsonify(response.json()['response'])
    results.headers.add('Access-Control-Allow-Origin','*')
    return results