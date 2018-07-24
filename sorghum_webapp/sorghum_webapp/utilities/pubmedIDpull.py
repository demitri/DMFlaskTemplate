from litter_getter import pubmed
# import xml.dom.minidom
import xml.etree.ElementTree as ET

# register with user account
pubmed.connect("PUBMED", 'muna@cshl.edu')

def getMetaDAta(papersToFind):

	ids = []
	for paper in papersToFind:
		ids.append(paper.pubmed_id)

	fetch = pubmed.PubMedFetch(id_list=ids)
	refs = fetch.get_content()

	for num, id in enumerate(refs):
		if papersToFind[num].s.title.lower() = refs[num]['title'].lower():
			papersToFind[num].abstract = refs[num]['abstract']
			papersToFind[num].paper_authors = ', '.join(refs[num]['authors_list'])
			papersToFind[num].source_url = "https://www.ncbi.nlm.nih.gov/pubmed/" + papersToFind[num].pubmed_id

			root = ET.fromstring(refs[num]["xml"])

			for pubDate in root[1][0].findall('PubMedPubDate'):
				if pubDate.get('PubStatus') == 'pubmed':
					year = pubDate.find('Year').text
					month = pubDate.find('Month').text
					day = pubDate.find('Day').text
					break

			papersToFind[num].publication_date = year + "-" + month + "-" + day
		else:
			papersToFind[num].abstract = "The title and PubMed ID do not seem to match, please check."

	return papersToFind
