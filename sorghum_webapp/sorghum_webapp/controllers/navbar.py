import logging
app_logger = logging.getLogger("sorghumbase")

def make_menu(label, style='simple'):
    return { 'label':label, 'style':style, 'links':[] }

def add_link(menu, label, link):
    menu['links'].append({'label':label, 'link':link})

def news():
    menu = make_menu('News')
    add_link(menu, 'News', '/posts?categories=news')
    add_link(menu, 'Events', '/events')
    add_link(menu, 'Publications', '/publications')
    return menu

def community():
    menu = make_menu('Community')
    add_link(menu, 'Research Notes', '/posts?categories=researchnote')
    add_link(menu, 'People', '/people')
    add_link(menu, 'Mailing List', '/mailing_list')
    return menu

def resources():
    menu = make_menu('Resources')
    add_link(menu, 'Links', '/resource_links')
    add_link(menu, 'Tools', '/posts?categories=tools')
    add_link(menu, 'Tutorials', '/posts?categories=tutorials')
    add_link(menu, 'Projects', '/projects')
    return menu

def about():
    menu = make_menu('About')
    add_link(menu, 'Mission Statement', '/mission-statement')
    add_link(menu, 'FAQ', '/faq')
    add_link(menu, 'Contact Us', '/contact')
    return menu

def genomes():
    ref = make_menu('Reference')
    add_link(ref, 'BTx723 - PI 564163', '#')
    add_link(ref, 'Rio - PI 651496', '#')

    sap = make_menu('SAP')
    bap = make_menu('BAP')
    ems = make_menu('EMS')

    menu = make_menu('Genomes','mega')
    menu['categories'] = [ref,sap,bap,ems]

    return menu

def navbar_template():
    return {'navbar': [news(), community(), genomes(), resources(), about()]}