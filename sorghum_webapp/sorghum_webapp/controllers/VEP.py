# #!/usr/bin/python
#
# # from flask import request #, make_response
# import os
# import flask
# from flask import request, render_template
# import json
# from urllib.request import urlopen
#
# import wordpress_orm as wp
# from wordpress_orm import wp_session, exc
#
# from .. import app
# from .. import wordpress_api as api
# from . import valueFromRequest
# from .navbar import navbar_template
# from .footer import populate_footer_template
#
# import mysql.connector
#
# mydb = mysql.connector.connect(
# 	host= 'cabot',
# 	user= os.environ['CABOT_USERNAME'],
# 	passwd= os.environ['CABOT_PASSWORD'],
# 	database='sorghum_bicolor_variation_58_93_30'
# )
# mycursor = mydb.cursor()
#
# WP_BASE_URL = app.config["WP_BASE_URL"]
#
# VEP_entry_page = flask.Blueprint("VEP_entry_page", __name__)
# VEP_source_page = flask.Blueprint("VEP_source_page", __name__)
# VEP_page = flask.Blueprint("VEP_page", __name__)
#
# @VEP_entry_page.route('/VEP/<source>/<gene>')
# def VEP_entry(source, gene):
# 	'''
# 	This page displays a single VEP entry based on gene and study.
# 	'''
# 	templateDict = navbar_template()
# 	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")
#
# 	with api.Session():
#
# 		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")
#
# 		populate_footer_template(wp_api=api, template_dictionary=templateDict, photos_to_credit=[])
#
# 	templateDict["sorghum_grains_image"] = sorghum_grains_image
#
# 	# url = "http://brie:8984/solr/sorghum_transcripts58/query?q=" + gene + "&fl=transcript_id,id,name,vep__" + source + "__*"
# 	url = "http://brie:8984/solr/sorghum_transcripts58/query?q=Sb02g026200&fl=transcript_id,id,name,vep__" + source + "__*"
#
# 	response = urlopen(url)
# 	vep_item = json.loads(response.read())
# 	sample_no = []
#
# 	for key in vep_item["response"]["docs"][0]:
# 		if key[:3] == "vep" and key[-3:] != 'any':
# 			sample_no = vep_item["response"]["docs"][0][key]
# 			if int(source) > 9:
# 				vep_type = key[9:]
# 			else:
# 				vep_type = key[8:]
#
# 	t_sample_no = tuple(sample_no)
#
# 	getSampleNames = "SELECT name FROM sample WHERE sample_id IN {}".format(t_sample_no)
#
# 	mycursor.execute(getSampleNames)
#
# 	sample_names = mycursor.fetchall()
#
# 	templateDict["sample"] = gene + " from study " + source
# 	templateDict["vep_item"] = vep_item
# 	templateDict["vep_type"] = vep_type
# 	templateDict["sample_names"] = sample_names
#
# 	#for c in post.comments:
# 	#	print(c)
# 	#logger.debug(" ============= controller finished ============= ")
# 	return render_template("VEP.html", **templateDict)
#
# @VEP_source_page.route('/VEP/<source>/')
# def VEP_source(source):
# 	'''
# 	This page displays a list of samples within a study.
# 	'''
# 	templateDict = navbar_template()
# 	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")
#
# 	with api.Session():
#
# 		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")
#
# 		populate_footer_template(wp_api=api, template_dictionary=templateDict, photos_to_credit=[])
#
# 	selectSamples = "SELECT sample_id, name FROM sample WHERE study_id = %s"
#
# 	# selectSamples = "SELECT sa.sample_id, sa.name FROM sample sa, study st WHERE sa.study_id = st.source_id"
# 	t_source = (int(source), )
# 	mycursor.execute(selectSamples, t_source)
#
# 	study_samples = mycursor.fetchall()
#
# 	templateDict["sorghum_grains_image"] = sorghum_grains_image
# 	templateDict["source"] = source
# 	templateDict["source_title"] = "needtoget"
# 	templateDict["study_samples"] = study_samples
#
# 	#for c in post.comments:
# 	#	print(c)
# 	#logger.debug(" ============= controller finished ============= ")
# 	return render_template("VEP.html", **templateDict)
#
# @VEP_page.route('/VEP')
# def VEP():
# 	'''
# 	This page a list of studies that have samples with VEPs.
# 	'''
# 	templateDict = navbar_template()
#
# 	#api = wp.API(url="http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/")
#
# 	with api.Session():
#
# 		sorghum_grains_image = api.media(slug="sorghum-grains_1920x1000")
#
# 		populate_footer_template(wp_api=api, template_dictionary=templateDict, photos_to_credit=[])
#
# 	selectStudies = "SELECT study_id, source_id, name FROM study"
#
# 	mycursor.execute(selectStudies)
#
# 	templateDict["sorghum_grains_image"] = sorghum_grains_image
# 	templateDict["VEP"] = True
# 	templateDict["studies"] = mycursor.fetchall()
#
# 	#for c in post.comments:
# 	#	print(c)
# 	#logger.debug(" ============= controller finished ============= ")
# 	return render_template("VEP.html", **templateDict)
