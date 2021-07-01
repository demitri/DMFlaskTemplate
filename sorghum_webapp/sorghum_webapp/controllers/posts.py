#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm_extensions.germplasm import GermplasmRequest
from ..wordpress_orm_extensions.population import PopulationRequest
from math import ceil

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

post_grid = flask.Blueprint("post_grid", __name__)
germplasm_grid = flask.Blueprint("germplasm_grid", __name__)
population_grid = flask.Blueprint("population_grid", __name__)

WAY_MORE_THAN_WE_WILL_EVER_HAVE = 100
spacer = " & "


@post_grid.route('/posts')
def posts():
	''' List of posts '''
	current_page = valueFromRequest(key="page", request=request) or 1
	if type(current_page) is str:
		current_page = int(current_page)
	n_per_page = valueFromRequest(key="show", request=request) or 9
	categories = valueFromRequest(key="categories", request=request, aslist=True)
	active_menu = 'Resources'
	if categories[0] == 'news':
		active_menu = 'News'
	if categories[0] == 'researchnote':
		active_menu = 'Community'
	templateDict = navbar_template(active_menu)

	with api.Session():

		post_count = api.PostRequest()
		if categories:
			post_count.categories = categories
		post_count.categories_exclude = ["faq", 17]  # 17 is the category for Sorghumbase CMS Tutorials
		post_count.per_page = WAY_MORE_THAN_WE_WILL_EVER_HAVE
		post_tally = post_count.get(count=True)

		post_request = api.PostRequest()
		if categories:
			post_request.categories = categories
		post_request.categories_exclude = ["faq", 17]  # 17 is the category for Sorghumbase CMS Tutorials
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = n_per_page
		post_request.page = current_page

		posts = post_request.get(count=False)
		if isinstance(categories, list) and 'blog' in categories:
			posts_banner_media = api.media(slug="sorghum_combine")
		else:
			posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")

		templateDict["banner_media"] = posts_banner_media

		# pre-cache these items so new HTTP connections aren't made from the template
		for p in posts:
			p.categories
			p.author

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['posts'] = posts
	templateDict['post_tally'] = post_tally
	if categories:
		templateDict['categories'] = spacer.join(categories)
	else:
		templateDict['categories'] = 'posts'
	templateDict['current_page'] = current_page
	templateDict['previous_page'] = max([current_page - 1, 0])
	templateDict['next_page'] = min([current_page + 1, ceil(post_tally / n_per_page)])
	templateDict['n_per_page'] = n_per_page
	logger.debug(" ============= controller finished ============= ")

	return render_template("posts.html", **templateDict)

@germplasm_grid.route('/germplasms')
def germplasms():
	''' List of germplasms '''

	# templateDict = navbar_template(active_menu)
	templateDict = navbar_template('Germplasms')

	with api.Session():

		germplasm_request = GermplasmRequest(api=api)
		germplasms = germplasm_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media
		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['posts'] = germplasms
	templateDict['post_type'] = "Germplasms"

	return render_template("post_list.html", **templateDict)

@population_grid.route('/populations')
def populations():
	''' List of populations '''

	# templateDict = navbar_template(active_menu)
	templateDict = navbar_template('Germplasms')

	with api.Session():

		population_request = PopulationRequest(api=api)
		populations = population_request.get()

		posts_banner_media = api.media(slug="k-state-sorghum-field-1920x1000")
		templateDict["banner_media"] = posts_banner_media
		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[posts_banner_media])

	templateDict['posts'] = populations
	templateDict['post_type'] = "Populations"

	return render_template("post_list.html", **templateDict)
