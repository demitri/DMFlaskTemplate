
import wordpress_orm as wp
from wordpress_orm import wp_session, exc

def populate_footer_template(template_dictionary=None, wp_api=None, photos_to_credit=list()):
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
		if post.featured_media:
			photos_to_credit.append(post.featured_media)

	#remove duplicates
	photos_to_credit = list(set(photos_to_credit))

	photographers = []
	filtered_photographs = []
	for photo in photos_to_credit:
		if photo.s.alt_text not in photographers:
			photographers.append(photo.s.alt_text)
			filtered_photographs.append(photo)

	if photos_to_credit:
		template_dictionary["photos_to_credit"] = filtered_photographs
	template_dictionary["footer_latest_news"] = posts
