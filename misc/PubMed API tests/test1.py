#!/usr/bin/env python

'''
This script performs a PubMed search and returns a list of article IDs.
'''

from litter_getter import pubmed

pubmed.connect("PUBMED", 'muna@cshl.edu')

#search_term = """science[journal] AND sorghum AND 2018[pdat]"""
search_term = """science[journal] AND breast cancer AND 2008[pdat]"""
search = pubmed.PubMedSearch(term=search_term)

search.get_ids_count()

print("ID count: {0}".format(search.id_count))

id_list = search.get_ids()

print("IDs: {0}".format(id_list))
