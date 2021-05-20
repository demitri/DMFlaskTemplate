#!/usr/bin/python

# This is the home page of the site.

import os
import json
import logging

import flask
import requests
from flask import send_from_directory
#from flask import request, render_template, send_from_directory
#from flask import current_app
from flask import render_template, request
import wordpress_orm as wp
from wordpress_orm import wp_session, exc
from random import randint

from . import valueFromRequest
from .. import app
from .. import wordpress_api as api
from .navbar import navbar_template
from .footer import populate_footer_template
from ..wordpress_orm_extensions.user import SBUser

#
# Note on WordPress queries. Not all information needed is returned by
# API calls. It's convenient to perform additional requests as needed
# here in the controller, but to append the data directly to records.
# To avoid stepping on any reserved words, prepend a "+" to any
# custom values added to a record.
#

#WP_BASE_URL = app.config["WP_BASE_URL"]
#logger = logging.getLogger("wordpress_orm")
#console_handler = logging.StreamHandler()
#logger.addHandler(console_handler)
#logger.propagate = False

app_logger = logging.getLogger("sorghumbase")
wp_logger = logging.getLogger("wordpress_orm")

index_page = flask.Blueprint("index_page", __name__)

@index_page.route("/", methods=['GET'])
def index():
	'''
	Home page
	'''

	templateDict = navbar_template()

	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")

	# perform all WordPress requests in a single session
	with api.Session():

		post_request = api.PostRequest()
		post_request.categories = ["researchnote"]	# search by slug
		post_request.orderby = "date"
		post_request.order = "desc"
		post_request.per_page = 3			# only get three newest

		posts = post_request.get()

		small_banner = api.media(slug="sorghum-grains_1920x1000")
		templateDict["small_banner"] = small_banner
		big_banner_1 = api.media(slug="sorghum_sky_darker")
		templateDict["big_banner_1"] = big_banner_1
		banners = []
		genes_banner = {"id" : "genes", "group": "Data"}
		genes_banner["media"] = api.media(slug="gene_search_banner3")
		genes_banner["link_url"] = "/genes"
		genes_banner["link_text"] = "Explore Genes"
		genes_banner["title"] = "Pan-genome resources"
		genes_banner["format"] = "left"
# 		banners.append(genes_banner)
		ta_banner = {"id" : "type-ahead", "group": "Type-ahead search: Select filters to search or refine a search"}
		ta_banner["media"] = api.media(slug="type-ahead")
		ta_banner["video"] = api.media(slug="type-ahead-video")
		ta_banner["link_url"] = "/genes"
		ta_banner["link_text"] = "Try it!"
		ta_banner["title"] = "type-ahead search"
		ta_banner["format"] = "video"
		banners.append(ta_banner)
		pg_banner = {"id" : "pan-genome-dist", "group": "Visualize genomic positions of genes containing the NB-ARC InterPro domain. This domain is often found in disease resistance genes."}
		pg_banner["media"] = api.media(slug="pan-genome-dist")
		pg_banner["link_url"] = "/genes?filters={%22status%22:%22init%22,%22operation%22:%22AND%22,%22negate%22:false,%22marked%22:false,%22leftIdx%22:0,%22rightIdx%22:3,%22children%22:[{%22fq_field%22:%22domains__ancestors%22,%22fq_value%22:%222182%22,%22name%22:%22NB-ARC%22,%22category%22:%22InterPro%20Domain%22,%22leftIdx%22:1,%22rightIdx%22:2,%22negate%22:false,%22showMenu%22:false,%22marked%22:true}],%22showMarked%22:true,%22showMenu%22:false,%22moveCopyMode%22:%22%22,%22searchOffset%22:0,%22rows%22:20}&genomes="
		pg_banner["link_text"] = "Explore"
		pg_banner["title"] = "pan-genome distribution"
		pg_banner["format"] = "wide"
		banners.append(pg_banner)
		gn_banner = {"id" : "neighbors", "group": "Inspect regions surrounding orthologs for copy number variation"}
		gn_banner["media"] = api.media(slug="yellow-seed1-neighborhood")
		gn_banner["link_url"] = "/genes"
		gn_banner["link_text"] = "Try it!"
		gn_banner["title"] = "gene neighborhood"
		gn_banner["format"] = "wide"
		banners.append(gn_banner)
		fo_banner = {"id" : "family-overview", "group": "Compare differences in functional annotation within gene families"}
		fo_banner["media"] = api.media(slug="yellow-seed1-overview")
		fo_banner["link_url"] = "/genes"
		fo_banner["link_text"] = "Try it!"
		fo_banner["title"] = "family overview"
		fo_banner["format"] = "wide"
		banners.append(fo_banner)
		msa_banner = {"id" : "msa", "group": "Find segregating alleles in coding regions"}
		msa_banner["media"] = api.media(slug="yellow-seed1-msa")
		msa_banner["link_url"] = "/genes"
		msa_banner["link_text"] = "Try it!"
		msa_banner["title"] = "multiple sequence alignment"
		msa_banner["format"] = "wide"
		banners.append(msa_banner)


		templateDict["banners"] = banners
		big_banner_3 = api.media(slug="sorghum_sky")
		templateDict["big_banner_3"] = big_banner_3

		photos_to_credit = [big_banner_1, big_banner_3, small_banner]

		user_request = api.UserRequest()
		user_request.context = "edit"
		user_request.per_page = 50
		user_request.roles = ["team_member"]
		users = user_request.get(class_object=SBUser)

		# Way to check if WP access is authenticated - all users would be returned in that case,
		# not just the ones who have posted.
		#for u in users:
		#	wp_logger.debug("User: {0}".format(u.s.name))

		tool_request = api.PostRequest()
		tool_request.categories = ["tools"]	# search by slug
		tools = tool_request.get()

		someUsers = []
		someTools = []

		for x in range(3):
			index = randint(0, len(users)-1)
			someUsers.append(users.pop(index))

		for x in range(min(3, len(tools))):
			index = randint(0, len(tools)-1)
			someTools.append(tools.pop(index))

		if len(posts) == 0:
			# Try to do some troubleshooting.

			# Is the 'blog' category defined?
			blog_category = None
			try:
				blog_category = api.category(slug="researchnote")
			except wp.exc.NoEntityFound:
				wp_logger.debug("Expected to find the 'Blog' category (identified by the slug 'blog') but not found!")

			if blog_category is not None:
				wp_logger.debug("The 'blog' category was found, but (maybe?) no posts are flagged with that category.")

		# fetch linked objects we know we'll need while we have this open connection
		for post in posts:
			photos_to_credit.append(post.featured_media)

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=photos_to_credit)

	#for post in posts:
	#	print(post.featured_media.s.link, post.featured_media.s.source_url)
	templateDict["team"] = someUsers
	templateDict["tools"] = someTools
	templateDict["toolicons"] = ["icon-layers", "icon-telescope", "icon-globe"]
	templateDict["posts"] = posts
	app_logger.debug(" ============= controller finished ============= ")
	return render_template("index.html", **templateDict, zip=zip)
