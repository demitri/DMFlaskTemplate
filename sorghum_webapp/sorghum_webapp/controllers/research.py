#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

from ..utilities.pubmedIDpull import getMetaData

from .. import app
from .. import wordpress_api as api
from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .footer import populate_footer_template

logger = logging.getLogger("wordpress_orm")

research_page = flask.Blueprint("research_page", __name__)

WAY_MORE_THAN_WE_WILL_EVER_HAVE = 100
@research_page.route('/research')
def research():
	''' List of research papers '''
	templateDict = {}

	with wp_session(api):
		paper_request = ScientificPaperRequest(api=api)

		papers = paper_request.get()

		queryPubmed = []

		for num, paper in enumerate(papers):
			if paper.abstract is "":
				if paper.pubmed_id is "":
					papers.pop(num)
				else:
					queryPubmed.append(papers.pop(num))

		info = getMetaData(queryPubmed)

		for paper in info:
			if paper.s.paper_authors is not "":
				papers.append(paper)

		papersByDate = sorted(papers, reverse=True, key=lambda k: k.publication_date)

		news_banner_media = api.media(slug="sorghum_panicle")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict['papers'] = papersByDate

	logger.debug(" ============= controller finished ============= ")

	return render_template("research.html", **templateDict)
