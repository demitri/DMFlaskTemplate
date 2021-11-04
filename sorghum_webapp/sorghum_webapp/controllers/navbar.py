import logging
app_logger = logging.getLogger("sorghumbase")

def make_menu(label, style='simple'):
    return { 'label':label, 'style':style, 'links':[] }

def add_link(menu, label, link):
    menu['links'].append({'label':label, 'link':link})

def news():
    menu = make_menu('News')
    add_link(menu, 'News', '/posts?categories=news')
    add_link(menu, 'Meetings & Events', '/events')
#     add_link(menu, 'Job Postings', '/jobs')
#     add_link(menu, 'Publications', '/publications')
    add_link(menu, 'Release Notes', '/relnotes')
    return menu

def engage():
    menu = make_menu('Engage')
#     add_link(menu, 'Research Notes', '/posts?categories=researchnote')
    add_link(menu, 'Training Materials', '/guides')
    add_link(menu, 'Videos', 'https://www.youtube.com/channel/UCXpgZNk1JDIn0-7AaS4EBxQ')
#     add_link(menu, 'Office Hours', '/office_hours')
    add_link(menu, 'Mailing List', '/mailing_list')
    add_link(menu, 'Contact Us', '/contact')
    return menu

def genomes():
    ref = make_menu('Genomes')
    add_link(ref, 'Species table','https://ensembl-dev.sorghumbase.org/species.html')
    add_link(ref, '--Browser Links--','none')
    add_link(ref, 'PI 564163 - BTx623', 'https://ensembl-dev.sorghumbase.org/Sorghum_bicolor')
    add_link(ref, 'PI 651496 - Rio', 'https://ensembl-dev.sorghumbase.org/Sorghum_rio')
    add_link(ref, 'PI 655996 - Tx430', 'https://ensembl-dev.sorghumbase.org/Sorghum_tx430nano')
    add_link(ref, 'PI 561071 - Tx436', 'https://ensembl-dev.sorghumbase.org/Sorghum_tx436pac')
    add_link(ref, 'PI 656001 - Tx2783', 'https://ensembl-dev.sorghumbase.org/Sorghum_tx2783pac')
    add_link(ref, 'IS12661', 'https://ensembl-dev.sorghumbase.org/Sorghum_is12661')
    add_link(ref, 'IS3614-3', 'https://ensembl-dev.sorghumbase.org/Sorghum_is36143')
    add_link(ref, 'IS38525', 'https://ensembl-dev.sorghumbase.org/Sorghum_is38525')
    add_link(ref, 'IS929', 'https://ensembl-dev.sorghumbase.org/Sorghum_is929')
    add_link(ref, 'Ji2731', 'https://ensembl-dev.sorghumbase.org/Sorghum_ji2731')
    add_link(ref, 'R931945-2-2', 'https://ensembl-dev.sorghumbase.org/Sorghum_r93194522')
    add_link(ref, 'IS19953', 'https://ensembl-dev.sorghumbase.org/Sorghum_is19953')
    add_link(ref, 'PI525695', 'https://ensembl-dev.sorghumbase.org/Sorghum_pi525695')
    add_link(ref, 'PI532566', 'https://ensembl-dev.sorghumbase.org/Sorghum_pi532566')
    add_link(ref, 'AusTRCF317961', 'https://ensembl-dev.sorghumbase.org/Sorghum_austrcf317961')
    add_link(ref, '353', 'https://ensembl-dev.sorghumbase.org/Sorghum_is12661')
    add_link(ref, 'PI36008', 'https://ensembl-dev.sorghumbase.org/Sorghum_pi536008')
    add_link(ref, 'S369-1', 'https://ensembl-dev.sorghumbase.org/Sorghum_s3691')
#     add_link(ref, '', '')
#     add_link(ref, 'PI 564163 - BTx623', '/accession/btx623')
#     add_link(ref, 'PI 651496 - Rio', '/accession/rio')
#     add_link(ref, 'PI 655996 - Tx430', '/accession/rtx430')
#     add_link(ref, 'PI 561071 - Tx436', '/accession/rtx436')
#     add_link(ref, 'PI 656001 - Tx2783', '/accession/tx2783')
    return ref

def germplasm():
    ref = make_menu('Reference')
    add_link(ref, 'PI 564163 - BTx623', '/accession/btx623')
    add_link(ref, 'PI 651496 - Rio', '/accession/rio')
    add_link(ref, 'PI 655996 - Tx430', '/accession/rtx430')
    add_link(ref, 'PI 561071 - Tx436', '/accession/rtx436')
    add_link(ref, 'PI 656001 - Tx2783', '/accession/tx2783')

    reseq = make_menu('Resequencing')


    association = make_menu('Association Panels')
    add_link(association, 'World Core Collection', '/population/world-core')
    add_link(association, 'Mini Core Collection', '/population/mini-core')
    add_link(association, 'Sorghum Association Panel', '/population/sap')
    add_link(association, 'Bioenergy Association Panel', '/population/bap')
    add_link(association, 'SCP + Exotic parents', '/population/scp-exotic')
    add_link(association, 'Expanded SCP Lines', '/population/expanded-scp')
    add_link(association, 'Nigerian Diversity Panel', '/population/nigeria-div')

    other = make_menu('EMS/NAM Populations')
    add_link(other, 'Xin EMS', '/population/xin-ems')
    add_link(other, 'Weil EMS', '/population/weil-ems')
    add_link(other, 'Klein BC-NAM', '/population/klein-nam')
    add_link(other, 'Kresovich NAM', '/population/kresovich-nam')
    add_link(other, 'Mace BC-NAM', '/population/mace-nam')

    menu = make_menu('Germplasm','mega')
    menu['categories'] = [ref, association, other, reseq]

    return menu

# def learn():
#     menu = make_menu('Learn')
#     add_link(menu, 'Tutorials (workflows)', '/#')
#     add_link(menu, 'Webinars', '/#')
#     add_link(menu, 'FAQ', '/#')
#
#     return menu

def tools():
   menu = make_menu('Tools')
   add_link(menu, 'Gene Search','/genes')
   add_link(menu, 'Genome Browser','https://ensembl.sorghumbase.org')
   add_link(menu, 'BLAST','https://ensembl.sorghumbase.org/Tools/Blast')
   return menu

def community_resources():
    projects = make_menu('Projects')
    add_link(projects, 'EMS', '#')
    add_link(projects, 'Sequencing projects - SAP', '#')

    databases = make_menu('Databases')
    add_link(databases, 'NCBI GEO', 'https://www.ncbi.nlm.nih.gov/gds')
    add_link(databases, 'SorghumFDB', 'http://structuralbiology.cau.edu.cn/sorghum/index.html')
    add_link(databases, 'Grassius', 'http://grassius.org/grasstfdb.php')
    add_link(databases, 'GrainGenes', 'https://wheat.pw.usda.gov/GG3/')
    add_link(databases, 'GRIN Global', 'https://npgsweb.ars-grin.gov/gringlobal/search.aspx')
    add_link(databases, 'Crop-PAL2', 'http://crop-pal.org/')
    add_link(databases, 'OZ Sorghum', 'https://aussorgm.org.au/')
    add_link(databases, 'Morokoshi Sorghum Transcriptome', 'http://sorghum.riken.jp/morokoshi/Home.html')

#     tools = make_menu('Tools')

    platforms = make_menu('continued')
    add_link(platforms, 'Gramene', 'http://www.gramene.org')
    add_link(platforms, 'CyVerse', 'http://datacommons.cyverse.org/')
    add_link(platforms, 'SciApps', 'https://www.sciapps.org/')
    add_link(platforms, 'AgriGO', 'http://bioinfo.cau.edu.cn/agriGO/')
    add_link(platforms, 'AgBioData', 'https://www.agbiodata.org/')
    add_link(platforms, 'JGI Phytozome', 'https://phytozome.jgi.doe.gov/pz/portal.html#!info?alias=Org_Sbicolor')
    add_link(platforms, 'MaizeGDB', 'https://www.maizegdb.org/')

    research = make_menu('Research')
    add_link(research, 'Publications', '/publications')
    return research
    menu = make_menu('Community Resources','mega')
    menu['categories'] = [projects, databases, platforms, research]
    return menu

# def resources():
#     menu = make_menu('Community Resources')
#     add_link(menu, 'Links', '/resource_links')
#     add_link(menu, 'Tools', '/posts?categories=tools')
#     add_link(menu, 'Tutorials', '/posts?categories=tutorials')
#     add_link(menu, 'Projects', '/projects')
#     return menu

def about():
    menu = make_menu('About')
#     add_link(menu, 'Mission Statement', '/mission-statement')
    add_link(menu, 'Team', '/people')
    add_link(menu, 'Contact Us', '/contact')
#     add_link(menu, 'FAQ', '/faq')
#     add_link(menu, 'Feedback', '/feedback')
    return menu

def support():
    menu = make_menu('Support')
    add_link(menu, 'New to SorghumBase', '#')
    add_link(menu, 'Troubleshooting', '#')
    add_link(menu, 'Help Board', '#')
    return menu

def navbar_template(activemenu='NA'):
    return {'navbar': [news(), engage(), genomes(), tools(), community_resources(), about()],'activemenu':activemenu}
#     return {'navbar': [news(), engage(), germplasm(), tools(), community_resources(), about()],'activemenu':activemenu}
