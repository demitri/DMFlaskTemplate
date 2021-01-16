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
    add_link(menu, 'Job Postings', '/jobs')
    add_link(menu, 'Publications', '/publications')
    add_link(menu, 'Release Notes', '/#')
    return menu

def engage():
    menu = make_menu('Engage')
    add_link(menu, 'Research Notes', '/posts?categories=researchnote')
    add_link(menu, 'Office Hours', '/#')
    add_link(menu, 'Mailing List', '/mailing_list')
    return menu

def genomes():
    ref = make_menu('Genomes')
    add_link(ref, 'BTx623 - PI 564163', '/accession/btx623')
    add_link(ref, 'Rio - PI 651496', '/accession/rio')
    add_link(ref, 'RTx430 - PI 655996', '/accession/rtx430')
    add_link(ref, 'RTx436 - PI 561071', '/accession/rtx436')
    add_link(ref, 'Tx2783 - PI 656001', '/accession/tx2783')
    return ref

def germplasm():
    ref = make_menu('Reference')
    add_link(ref, 'BTx623 - PI 564163', '/accession/btx623')
    add_link(ref, 'Rio - PI 651496', '/accession/rio')
    add_link(ref, 'RTx430 - PI 655996', '/accession/rtx430')
    add_link(ref, 'RTx436 - PI 561071', '/accession/rtx436')
    add_link(ref, 'Tx2783 - PI 656001', '/accession/tx2783')

    reseq = make_menu('Resequencing')


    association = make_menu('Association Panels')
    add_link(association, 'World Core Collection', '/population/world-core')
    add_link(association, 'Mini Core Collection', '/population/mini-core')
    add_link(association, 'Sorghum Association Panel', '/population/sap')
    add_link(association, 'Bioenergy Association Panel', '/population/bap')
    add_link(association, 'SCP + Exotic parents', '/population/scp-exotic')
    add_link(association, 'Expanded SCP Lines', '/population/expanded-scp')
    add_link(association, 'Nigerian Diversity Panel', '/population/nigeria-div')

    other = make_menu('Other Populations')
    add_link(other, 'Xin EMS', '/population/xin-ems')
    add_link(other, 'Weil EMS', '/population/weil-ems')
    add_link(other, 'Klein BC-NAM', '/population/klein-nam')
    add_link(other, 'Kresovich NAM', '/population/kresovich-nam')
    add_link(other, 'Mace BC-NAM', '/population/mace-nam')

    menu = make_menu('Germplasm','mega')
    menu['categories'] = [ref, reseq, association, other]

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
   add_link(menu, 'Gene Search','/genes/')
   add_link(menu, 'Genome Browser','http://banon.cshl.edu:88')
   add_link(menu, 'BLAST','#')
   return menu

def community_resources():
    projects = make_menu('Projects')
    add_link(projects, 'EMS', '#')
    add_link(projects, 'Sequencing projects - SAP', '#')

    databases = make_menu('Databases')
    add_link(databases, 'NCBI GEO', '#')
    add_link(databases, 'SorghumFDB', '#')
    add_link(databases, 'Grassius', '#')
    add_link(databases, 'GrainGenes', '#')
    add_link(databases, 'GRIN Global', '#')
    add_link(databases, 'Crop-PAL2', '#')
    add_link(databases, 'OZ Sorghum', '#')
    add_link(databases, 'Morokoshi Sorghum Transcription DB', '#')

    tools = make_menu('Tools')
    add_link(tools, 'Ensembl Browser', '#')
    add_link(tools, 'Gene Search', '#')
    add_link(tools, 'BLAST', '#')
    add_link(tools, 'SciApps', '#')
    add_link(tools, 'AgriGO', '#')

    platforms = make_menu('Platforms/Portals')
    add_link(platforms, 'Gramene', '#')
    add_link(platforms, 'CyVerse', '#')
    add_link(platforms, 'AgBioData', '#')
    add_link(platforms, 'JGI Phytozome', '#')
    add_link(platforms, 'MaizeGDB', '#')

    menu = make_menu('Community Resources','mega')
    menu['categories'] = [projects, databases, tools, platforms]
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
    add_link(menu, 'Mission Statement', '/mission-statement')
    add_link(menu, 'Team', '/people')
    add_link(menu, 'FAQ', '/faq')
    add_link(menu, 'Contact Us', '/contact')
    return menu

def support():
    menu = make_menu('Support')
    add_link(menu, 'New to SorghumBase', '#')
    add_link(menu, 'Troubleshooting', '#')
    add_link(menu, 'Help Board', '#')
    return menu

def navbar_template(activemenu='NA'):
    return {'navbar': [news(), engage(), genomes(), tools(), community_resources(), about()],'activemenu':activemenu}
#     return {'navbar': [news(), engage(), germplasm(), community_resources(), about()],'activemenu':activemenu}
