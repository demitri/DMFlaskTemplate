#!/usr/bin/python

# from flask import request #, make_response

import flask
import logging
import json
from flask import request, render_template
from wordpress_orm import wp_session
from wordpress_orm.entities import Tag
from ..wordpress_orm_extensions.scientific_paper import ScientificPaperRequest

from ..utilities.pubmedIDpull import getMetaData

from .. import app
from .. import wordpress_api as api
#from .. import wordpress_orm_logger as wp_logger
from . import valueFromRequest
from .navbar import navbar_template
from .footer import populate_footer_template

#logger = logging.getLogger("wordpress_orm")
wp_logger = logging.getLogger("wordpress_orm")
app_logger = logging.getLogger("sorghumbase")

publications_page = flask.Blueprint("publications_page", __name__)

WAY_MORE_THAN_WE_WILL_EVER_HAVE = 100
@publications_page.route('/publications')
def publications():
	''' List of research papers '''
	templateDict = navbar_template('News')

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
				paper.s.content = paper.s.abstract
				if not len(paper.s.paper_authors) == 0 :
					if paper.s.keywords != "No keywords in Pubmed":
						paper_tags = []
						kwl = paper.s.keywords.split(',')
						kwd = [w.strip() for w in kwl]
						for keyword in kwd:
							new_tag = Tag(api=api)
							new_tag.s.name = keyword
							tag_id = str(new_tag.post)
							paper_tags.append(tag_id)
						paper.s.tags = ', '.join(paper_tags)
					paper.update()
					papersWithInfo.append(paper)

		all_keywords = set()
		all_years = []
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

		for paper in papersByDate:
			if paper.s.publication_date[:4] not in all_years:
				all_years.append(paper.s.publication_date[:4])

		news_banner_media = api.media(slug="sorghum_panicle")
		templateDict["banner_media"] = news_banner_media

		populate_footer_template(template_dictionary=templateDict, wp_api=api, photos_to_credit=[news_banner_media])

	templateDict['papers'] = papersByDate
	templateDict['keywords'] = all_keywords
	templateDict['years'] = all_years

	app_logger.debug(" ============= controller finished ============= ")

	# return render_template("publications.html", **templateDict)
	return render_template("research_filter.html", **templateDict)
