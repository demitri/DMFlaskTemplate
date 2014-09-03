#!/usr/bin/python

'''
This file contains all custom Jinja2 filters.
'''

import jinja2
import flask

blueprint = flask.Blueprint('jinja_filters', __name__)

# Ref: http://stackoverflow.com/questions/12288454/how-to-import-custom-jinja2-filters-from-another-file-and-using-flask

# place these decorators above every filter
@jinja2.contextfilter
@blueprint.app_template_filter()
def j2split(value, delimiter=None):
	if delimiter == None:
		return value.split()
	else:
		return value.split(delimiter)

@jinja2.contextfilter
@blueprint.app_template_filter()
def j2join(value, delimiter=","):
    return delimiter.join(value)

