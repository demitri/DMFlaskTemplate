#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
import json
from flask import request, render_template
from wordpress_orm import wp_session
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

from ..utilities.pubmedIDpull import getMetaData

from .. import app
from .. import wordpress_api as api
#from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .footer import populate_footer_template

#logger = logging.getLogger("wordpress_orm")
wp_logger = logging.getLogger("wordpress_orm")
app_logger = logging.getLogger("sorghumbase")

publications_page = flask.Blueprint("publications_page", __name__)

WAY_MORE_THAN_WE_WILL_EVER_HAVE = 100
@publications_page.route('/publications')
def publications():
	''' List of research papers '''
	templateDict = {}

	with api.Session():
		paper_request = ScientificPaperRequest(api=api)
		paper_request.per_page = 50
		rawPapers = paper_request.get()
		print(len(rawPapers))

		papersWithInfo = [p for p in rawPapers if not (len(p.s.abstract) == 0 or len(p.s.keywords) == 0) or len(p.s.pubmed_id) == 0]

		queryPubmed = [p for p in rawPapers if (len(p.s.abstract) == 0 or len(p.s.keywords) == 0 and not len(p.s.pubmed_id) == 0)]

		if len(queryPubmed) > 0:
			info = getMetaData(queryPubmed)

			for paper in info:
				if not len(paper.s.paper_authors) == 0:
					paper.update()
					papersWithInfo.append(paper)

		all_keywords = set()

		# toggle = True
		# for paper in papersWithInfo:
		# 	if toggle:
		# 		[all_keywords.add(x) for x in ['blue brown bear black', 'green', 'Black']]
		# 		paper.kwd = json.dumps(['blue brown bear black', 'green', 'Black'])
		# 		toggle = False
		# 	else:
		# 		[all_keywords.add(x) for x in ["orange/", "yellow9", "red"]]
		# 		paper.kwd = json.dumps(["orange/", "yellow9", "red"])
		# 		toggle = True

		for paper in papersWithInfo:
			if len(paper.s.keywords) > 0 and paper.s.keywords != "No keywords in Pubmed":
				kwl = paper.s.keywords.split(',')
				kwd = [w.strip() for w in kwl]
				[all_keywords.add(x) for x in kwd]

		papersByDate = sorted(papersWithInfo, reverse=True, key=lambda k: k.s.publication_date)

		news_banner_media = api.media(slug="sorghum_panicle")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict['papers'] = papersByDate
	templateDict['keywords'] = all_keywords

	app_logger.debug(" ============= controller finished ============= ")

	return render_template("publications.html", **templateDict)
