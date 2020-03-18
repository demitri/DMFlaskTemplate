#!/usr/bin/python

# from flask import request #, make_response

import flask
from flask import request, render_template

import wordpress_orm as wp
from wordpress_orm import wp_session, exc
from wordpress_orm.entities import Tag

from .. import app
from .. import wordpress_api as api
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template
from ..wordpress_orm_extensions.germplasm import GermplasmRequest
from ..wordpress_orm_extensions.population import PopulationRequest
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

WP_BASE_URL = app.config["WP_BASE_URL"]

post_page = flask.Blueprint("post_page", __name__)
post_category_page = flask.Blueprint("post_category_page", __name__)
population_page = flask.Blueprint("population_page", __name__)
genome_page = flask.Blueprint("genome_page", __name__)

@post_page.route('/post/<slug>')
def post(slug):
	'''
	This page displays a single blog post retrieved from WordPress.
	'''
	templateDict = navbar_template()

	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")

	with api.Session():
		# get the post based on the slug
		try:
			post = api.post(slug=slug)
		except exc.NoEntityFound:
			# TODO return top level posts page
			raise Exception("Return top level posts page, maybe with an alert of 'post not found'.")

		# Get the three latest "News" posts from WordPress.
		# -------------------------------------------------
		pr = api.PostRequest()
		pr.categories = ['news']	# accepts category slug values, not display name
		pr.order = "desc"			# descending order
		pr.per_page = 3				# only get three newest
		latest_posts = pr.get()

		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")

		populate_footer_template(wp_api=api, template_dictionary=templateDict, photos_to_credit=[])

		# pre-fetch relationships (premature optimization!)
		for p in latest_posts:
			p.categories


	templateDict["post"] = post
	templateDict["latest_posts"] = latest_posts
	templateDict["sorghum_grains_image"] = sorghum_grains_image
	templateDict["display_comments"] = False
	templateDict["allow_new_comments"] = False
	templateDict["author_gravatar_url"] = post.author.gravatar_url(size=140)

	#for c in post.comments:
	#	print(c)
	#logger.debug(" ============= controller finished ============= ")
	return render_template("post.html", **templateDict)

@post_category_page.route('/posts/category/<slug>')
def post_category(category_slug):
	'''
	This page displays a grid of post thumbnails from a given category.
	'''
	templateDict = {}

	return render_template("post_category.html", **templateDict)

@population_page.route('/population/<slug>')
def population(slug):
	'''
	This page displays a post describing a population.
	'''
	templateDict = navbar_template()

	with api.Session():

		try:
			population_request = PopulationRequest(api=api)
			population_request.slug = [slug]
			population = population_request.get()
		except exc.NoEntityFound:
			# TODO return top level posts page
			raise Exception("Population not found.")

		new_tag = Tag(api=api)
		new_tag.s.name = slug
		tag_id = str(new_tag.post)

		pr = api.PostRequest()
		pr.tags = [tag_id]
		tagged_posts = pr.get()

		spr = ScientificPaperRequest(api=api)
		spr.tags = [tag_id]
		spr.tags_exclude = [227]	# 227 is the tag ID for "original citation"
		tagged_publications = spr.get()



		cpr = ScientificPaperRequest(api=api)
		cpr.include = [population[0].s.original_citation]	# 227 is the tag ID for "original citation"
		citation = cpr.get()
		print(citation[0])

		gr = GermplasmRequest(api=api)
		gr.tags = [tag_id]
		tagged_germplasms = gr.get()

		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")

		templateDict["population"] = population[0]
		templateDict["related_posts"] = tagged_posts
		templateDict["citation"] = citation[0]
		templateDict["related_publications"] = tagged_publications
		templateDict["related_germplasms"] = tagged_germplasms
		templateDict["sorghum_grains_image"] = sorghum_grains_image

	return render_template("population.html", **templateDict)

@genome_page.route('/accession/<slug>')
def genome(slug):
	'''
	This page displays a post describing a germplasm.
	'''
	templateDict = navbar_template()

	with api.Session():

		try:
			germplasm_request = GermplasmRequest(api=api)
			germplasm_request.slug = ["g-" + slug]
			germplasm = germplasm_request.get()
		except exc.NoEntityFound:
			# TODO return top level posts page
			raise Exception("Germplasm not found.")

		new_tag = Tag(api=api)
		new_tag.s.name = slug
		tag_id = str(new_tag.post)

		pr = api.PostRequest()
		pr.tags = [tag_id]
		tagged_posts = pr.get()

		spr = ScientificPaperRequest(api=api)
		spr.tags = [tag_id]
		tagged_publications = spr.get()

		popr = PopulationRequest(api=api)
		popr.tags = [tag_id]
		tagged_populations = popr.get()

		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")

		templateDict["population"] = germplasm[0]
		templateDict["related_posts"] = tagged_posts
		templateDict["related_publications"] = tagged_publications
		templateDict["related_populations"] = tagged_populations
		templateDict["sorghum_grains_image"] = sorghum_grains_image

	return render_template("population.html", **templateDict)
