from litter_getter import pubmed
# import xml.dom.minidom
import xml.etree.ElementTree as ET

# register with user account
pubmed.connect("PUBMED", 'muna@cshl.edu')

def getMetaData(papersToFind):

	ids = []
	for paper in papersToFind:
		ids.append(paper.s.pubmed_id)

	fetch = pubmed.PubMedFetch(id_list=ids)
	refs = fetch.get_content()

	for num, id in enumerate(refs):
		if papersToFind[num].s.title.lower() == refs[num]['title'].lower():
			papersToFind[num].s.abstract = refs[num]['abstract']
			papersToFind[num].s.paper_authors = ', '.join(refs[num]['authors_list'])
			papersToFind[num].s.source_url = "https://www.ncbi.nlm.nih.gov/pubmed/" + papersToFind[num].pubmed_id

			root = ET.fromstring(refs[num]["xml"])

			for pubDate in root[1][0].findall('PubMedPubDate'):
				if pubDate.get('PubStatus') == 'pubmed':
					year = pubDate.find('Year').text
					month = pubDate.find('Month').text
					day = pubDate.find('Day').text
					break

			papersToFind[num].s.publication_date = year + "-" + month + "-" + day
		else:
			papersToFind[num].s.abstract = "The title and PubMed ID do not seem to match, please check."

	return papersToFind
