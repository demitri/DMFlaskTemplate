
import wordpress_orm as wp
from wordpress_orm import wp_session, exc

def populate_footer_template(template_dictionary=None, wp_api=None, photos_to_credit=None):
	'''
	This function takes a template dictionary and populates the information needed for the footer.
	
	To avoid stepping on the calling template, all parameters here have the prefix "footer_".
	This function is expected to be called from within an existing "wp_session" 'with' block
	to avoid creating a new connection, but will work either way.
	'''

	if template_dictionary is None:
		raise Exception("A template dictionary must be provided.")
	elif wp_api is None:
		raise Exception("A wordpress_orm.API object must be provided.")
	
	# Get the three latest "News" posts from WordPress.
	# -------------------------------------------------
	pr = wp_api.PostRequest()
	pr.categories = ['news']	# accepts category slug values, not display name
	pr.order = "desc"			# descending order
	pr.per_page = 3				# only get three newest
	posts = pr.get()
	
	# while we're here, fetch the featured media
	for post in posts:
		post.featured_media
	
	# expect "photos_to_credit" to be a list of Media objects.
	#
	template_dictionary["footer_photos_to_credit"] = photos_to_credit
	template_dictionary["footer_latest_news"] = posts
