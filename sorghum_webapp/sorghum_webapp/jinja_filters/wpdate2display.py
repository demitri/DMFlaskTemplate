#!/usr/bin/python

'''
This is a Jinja 2 filter that converts an ISO-9001 date string to a string for display, e.g.

"2017-10-28T02:20:32" -> "28 October 2017"
'''

import flask
import jinja2
from jinja2 import Markup

# If the filter is to return HTML code and you don't want it autmatically
# escaped, return the value as "return Markup(value)".

blueprint = flask.Blueprint('jinja_filters', __name__)

# Ref: http://stackoverflow.com/questions/12288454/how-to-import-custom-jinja2-filters-from-another-file-and-using-flask

# place these two decorators above every filter
@jinja2.contextfilter
@blueprint.app_template_filter()
def j2split(context, value, delimiter=None):
	if delimiter == None:
		return value.split()
	else:
		return value.split(delimiter)

@jinja2.contextfilter
@blueprint.app_template_filter()
def j2join(context, value, delimiter=","):
    return delimiter.join(value)

