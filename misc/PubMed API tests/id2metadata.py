#!/usr/bin/env python

'''
This script takes a PubMed ID and retrieves the article metadata.
'''

from litter_getter import pubmed
import xml.etree.ElementTree as ET
import xml.dom.minidom

# register with user account
pubmed.connect("PUBMED", 'muna@cshl.edu')

ids = [29161754]  # Ref: https://www.ncbi.nlm.nih.gov/pubmed/29161754
fetch = pubmed.PubMedFetch(id_list=ids)
refs = fetch.get_content()

root = ET.fromstring(refs[0]["xml"])

keywordlist = root[0].find("KeywordList").findall("Keyword")

kwl =[]

for word in keywordlist:
	kwl.append((word.text).strip())

print(', '.join(kwl))

# "refs" is a list of dictionaries with keys:
'''
'xml' : the raw XML returned
'PMID' : PubMed ID
'title' : article title
'abstract' : article abstract
'citation' : citation, e.g. 'Plant J. 2018; 93 (2):338-354'
'year' : int
'doi' : DOI (string), e.g. '10.1111/tpj.13781'
'authors_list' : e.g. ['McCormick RF', 'Truong SK', 'Sreedasyam A', 'Jenkins J', 'Shu S', 'Sims D', 'Kennedy M', 'Amirebrahimi M', 'Weers BD', 'McKinley B', 'Mattison A', 'Morishige DT', 'Grimwood J', 'Schmutz J', 'Mullet JE']
'authors_short' : abbreviated, e.g. 'McCormick RF et al.'

Note that more information is available in the returned XML that doesn't appear to be
in the reference object created. This includes copyright information (<CopyrightInformation>),
author affiliations,
'''

#print(refs)

# ---------------------
# print XML to terminal
# ---------------------
# ref: https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python

# xml_string = refs[0]["xml"].replace("\n","")
# xml = xml.dom.minidom.parseString(xml_string)
# pretty_xml_string = xml.toprettyxml()
# print(pretty_xml_string)

"""
Result:

<?xml version="1.0" ?>
<PubmedArticle>
	<MedlineCitation Owner="NLM" Status="In-Process">
		<PMID Version="1">29161754</PMID>
		<DateRevised>
			<Year>2018</Year>
			<Month>01</Month>
			<Day>11</Day>
		</DateRevised>
		<Article PubModel="Print-Electronic">
			<Journal>
				<ISSN IssnType="Electronic">1365-313X</ISSN>
				<JournalIssue CitedMedium="Internet">
					<Volume>93</Volume>
					<Issue>2</Issue>
					<PubDate>
						<Year>2018</Year>
						<Month>01</Month>
					</PubDate>
				</JournalIssue>
				<Title>The Plant journal : for cell and molecular biology</Title>
				<ISOAbbreviation>Plant J.</ISOAbbreviation>
			</Journal>
			<ArticleTitle>The Sorghum bicolor reference genome: improved assembly, gene annotations, a transcriptome atlas, and signatures of genome organization.</ArticleTitle>
			<Pagination>
				<MedlinePgn>338-354</MedlinePgn>
			</Pagination>
			<ELocationID EIdType="doi" ValidYN="Y">10.1111/tpj.13781</ELocationID>
			<Abstract>
				<AbstractText>Sorghum bicolor is a drought tolerant C4 grass used for the production of grain, forage, sugar, and lignocellulosic biomass and a genetic model for C4 grasses due to its relatively small genome (approximately 800\xa0Mbp), diploid genetics, diverse germplasm, and colinearity with other C4 grass genomes. In this study, deep sequencing, genetic linkage analysis, and transcriptome data were used to produce and annotate a high-quality reference genome sequence. Reference genome sequence order was improved, 29.6\xa0Mbp of additional sequence was incorporated, the number of genes annotated increased 24% to 34\xa0211, average gene length and N50 increased, and error frequency was reduced 10-fold to 1 per 100\xa0kbp. Subtelomeric repeats with characteristics of Tandem Repeats in Miniature (TRIM) elements were identified at the termini of most chromosomes. Nucleosome occupancy predictions identified nucleosomes positioned immediately downstream of transcription start sites and at different densities across chromosomes. Alignment of more than 50 resequenced genomes from diverse sorghum genotypes to the reference genome identified approximately 7.4\xa0M single nucleotide polymorphisms (SNPs) and 1.9\xa0M indels. Large-scale variant features in euchromatin were identified with periodicities of approximately 25\xa0kbp. A transcriptome atlas of gene expression was constructed from 47 RNA-seq profiles of growing and developed tissues of the major plant organs (roots, leaves, stems, panicles, and seed) collected during the juvenile, vegetative and reproductive phases. Analysis of the transcriptome data indicated that tissue type and protein kinase expression had large influences on transcriptional profile clustering. The updated assembly, annotation, and transcriptome data represent a resource for C4 grass research and crop improvement.</AbstractText>
				<CopyrightInformation>© 2017 The Authors The Plant Journal © 2017 John Wiley &amp; Sons Ltd.</CopyrightInformation>
			</Abstract>
			<AuthorList CompleteYN="Y">
				<Author ValidYN="Y">
					<LastName>McCormick</LastName>
					<ForeName>Ryan F</ForeName>
					<Initials>RF</Initials>
					<AffiliationInfo>
						<Affiliation>Interdisciplinary Program in Genetics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Truong</LastName>
					<ForeName>Sandra K</ForeName>
					<Initials>SK</Initials>
					<AffiliationInfo>
						<Affiliation>Interdisciplinary Program in Genetics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Sreedasyam</LastName>
					<ForeName>Avinash</ForeName>
					<Initials>A</Initials>
					<AffiliationInfo>
						<Affiliation>HudsonAlpha Institute for Biotechnology, Huntsville, AL, 35806, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Jenkins</LastName>
					<ForeName>Jerry</ForeName>
					<Initials>J</Initials>
					<AffiliationInfo>
						<Affiliation>HudsonAlpha Institute for Biotechnology, Huntsville, AL, 35806, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Shu</LastName>
					<ForeName>Shengqiang</ForeName>
					<Initials>S</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Energy, Joint Genome Institute, Walnut Creek, CA, 94598, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Sims</LastName>
					<ForeName>David</ForeName>
					<Initials>D</Initials>
					<AffiliationInfo>
						<Affiliation>HudsonAlpha Institute for Biotechnology, Huntsville, AL, 35806, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Kennedy</LastName>
					<ForeName>Megan</ForeName>
					<Initials>M</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Energy, Joint Genome Institute, Walnut Creek, CA, 94598, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Amirebrahimi</LastName>
					<ForeName>Mojgan</ForeName>
					<Initials>M</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Energy, Joint Genome Institute, Walnut Creek, CA, 94598, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Weers</LastName>
					<ForeName>Brock D</ForeName>
					<Initials>BD</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>McKinley</LastName>
					<ForeName>Brian</ForeName>
					<Initials>B</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Mattison</LastName>
					<ForeName>Ashley</ForeName>
					<Initials>A</Initials>
					<AffiliationInfo>
						<Affiliation>Interdisciplinary Program in Genetics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Morishige</LastName>
					<ForeName>Daryl T</ForeName>
					<Initials>DT</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Grimwood</LastName>
					<ForeName>Jane</ForeName>
					<Initials>J</Initials>
					<AffiliationInfo>
						<Affiliation>HudsonAlpha Institute for Biotechnology, Huntsville, AL, 35806, USA.</Affiliation>
					</AffiliationInfo>
					<AffiliationInfo>
						<Affiliation>Department of Energy, Joint Genome Institute, Walnut Creek, CA, 94598, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Schmutz</LastName>
					<ForeName>Jeremy</ForeName>
					<Initials>J</Initials>
					<AffiliationInfo>
						<Affiliation>HudsonAlpha Institute for Biotechnology, Huntsville, AL, 35806, USA.</Affiliation>
					</AffiliationInfo>
					<AffiliationInfo>
						<Affiliation>Department of Energy, Joint Genome Institute, Walnut Creek, CA, 94598, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
				<Author ValidYN="Y">
					<LastName>Mullet</LastName>
					<ForeName>John E</ForeName>
					<Initials>JE</Initials>
					<AffiliationInfo>
						<Affiliation>Department of Biochemistry and Biophysics, Texas A&amp;M University, College Station, TX, 77843, USA.</Affiliation>
					</AffiliationInfo>
				</Author>
			</AuthorList>
			<Language>eng</Language>
			<PublicationTypeList>
				<PublicationType UI="D016428">Journal Article</PublicationType>
				<PublicationType UI="D013485">Research Support, Non-U.S. Gov\'t</PublicationType>
			</PublicationTypeList>
			<ArticleDate DateType="Electronic">
				<Year>2017</Year>
				<Month>12</Month>
				<Day>28</Day>
			</ArticleDate>
		</Article>
		<MedlineJournalInfo>
			<Country>England</Country>
			<MedlineTA>Plant J</MedlineTA>
			<NlmUniqueID>9207397</NlmUniqueID>
			<ISSNLinking>0960-7412</ISSNLinking>
		</MedlineJournalInfo>
		<KeywordList Owner="NOTNLM">
			<Keyword MajorTopicYN="Y">\nSorghum bicolor\n</Keyword>
			<Keyword MajorTopicYN="Y">discrete Fourier transform</Keyword>
			<Keyword MajorTopicYN="Y">gene annotation</Keyword>
			<Keyword MajorTopicYN="Y">genetic variation</Keyword>
			<Keyword MajorTopicYN="Y">genome assembly</Keyword>
			<Keyword MajorTopicYN="Y">kinase</Keyword>
			<Keyword MajorTopicYN="Y">nucleosome occupancy</Keyword>
			<Keyword MajorTopicYN="Y">reference genome</Keyword>
			<Keyword MajorTopicYN="Y">satellite DNA</Keyword>
		</KeywordList>
	</MedlineCitation>
	<PubmedData>
		<History>
			<PubMedPubDate PubStatus="received">
				<Year>2017</Year>
				<Month>04</Month>
				<Day>05</Day>
			</PubMedPubDate>
			<PubMedPubDate PubStatus="revised">
				<Year>2017</Year>
				<Month>11</Month>
				<Day>05</Day>
			</PubMedPubDate>
			<PubMedPubDate PubStatus="accepted">
				<Year>2017</Year>
				<Month>11</Month>
				<Day>14</Day>
			</PubMedPubDate>
			<PubMedPubDate PubStatus="pubmed">
				<Year>2017</Year>
				<Month>11</Month>
				<Day>22</Day>
				<Hour>6</Hour>
				<Minute>0</Minute>
			</PubMedPubDate>
			<PubMedPubDate PubStatus="medline">
				<Year>2017</Year>
				<Month>11</Month>
				<Day>22</Day>
				<Hour>6</Hour>
				<Minute>0</Minute>
			</PubMedPubDate>
			<PubMedPubDate PubStatus="entrez">
				<Year>2017</Year>
				<Month>11</Month>
				<Day>22</Day>
				<Hour>6</Hour>
				<Minute>0</Minute>
			</PubMedPubDate>
		</History>
		<PublicationStatus>ppublish</PublicationStatus>
		<ArticleIdList>
			<ArticleId IdType="pubmed">29161754</ArticleId>
			<ArticleId IdType="doi">10.1111/tpj.13781</ArticleId>
		</ArticleIdList>
	</PubmedData>
</PubmedArticle>
"""
