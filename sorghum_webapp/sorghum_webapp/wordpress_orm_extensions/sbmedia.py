'''

WordPress API reference: https://developer.wordpress.org/rest-api/reference/media/
'''

import os
import logging

import requests
from wordpress_orm import WPEntity, WPRequest, WPORMCacheObjectNotFoundError
from wordpress_orm.entities import Media as WPORMMedia

class SBMedia(WPORMMedia):
	
	def __init__(self, id=None, api=None):
		super().__init__(api=api)

		# related objects to cache
		self._author = None
		self._associated_post = None

	@property																			
	def schema_fields(self):
		return ["author_name", "comment_count", "comment_status", "comments", "guid",
				"id", "ID", "license_name", "license_url", "media_source_url",
				"menu_order", "ping_status", "pinged", "post_author", "post_content",
				"post_content_filtered", "post_date", "post_date_gmt", "post_excerpt",
				"post_mime_type", "post_modified", "post_modified_gmt", "post_name",
				"post_parent", "post_password", "post_status", "post_title",
				"post_type", "to_ping"]

class MediaRequest(WPRequest):

	def get(self, class_object=SBMedia):
		super().get(class_object=class_object)

	def postprocess_response(self):
		'''
		Perform additional processing of data returned from API.
		'''
		pass
	
