
'''

Custom WordPress object defined using the plugin WordPress Pods.

Ref: https://wordpress.org/plugins/pods/
'''

import logging
import requests

from wordpress_orm import WPEntity, WPRequest

logger = logging.getLogger("wordpress_orm")

class ResourceLink(WPEntity):
	
	def __init__(self, id=None, api=None):
		super().__init__(api=api)
		
		# related objects that need to be cached
		self._category = None
	
	def __repr__(self):
		if len(self.resource_url) < 11:
			truncated_url = self.s.resource_url
		else:
			truncated_url = self.s.resource_url[0:10] + "..."
		return "<WP {0} object at {1}, url='{2}'>".format(self.__class__.__name__, hex(id(self)),
																			self.s.id,
																			truncated_url)

	@property
	def schema_fields(self):
		return ["id", "date", "date_gmt", "guid", "modified", "modified_gmt",
				"slug", "status", "type", "link", "title", "content", "template",
				"resource_url", "resource_blurb", "resource_name", "category",
				"resource_author", "resource_image"]
	
	@property
	def categories(self):
		'''
		Returns a list of categories (as Category objects) associated with this post.
		'''
		if self._categories is None:
			self._categories = list()
			for category_id in self.s.categories:
				try:
					self._categories.append(self.api.category(id=category_id))
				except exc.NoEntityFound:
					logger.debug("Expected to find category ID={0} from post (ID={1}), but no category found.".format(category_id, self.s.id))
		return self._categories
	
	@property
	def category_names(self):
		return [x.s.name for x in self.categories]


class ResourceLinkRequest(WPRequest):
	'''
	A class that encapsulates requests for WordPress resource links.
	'''
	def __init__(self, api=None):		
		super().__init__(api=api)
		self.id = None # WordPress ID
		
		self._category_ids = list()
		self._slugs = list()
	
	@property
	def parameter_names(self):
		return ["slug"]
	
	def get(self):
		'''
		Returns a list of 'Resource Links' objects that match the parameters set in this object.
		'''
		self.url = self.api.base_url + "resource-link"
		
		if self.id:
			self.url += "/{}".format(self.id)
		
		# -------------------
		# populate parameters
		# -------------------
		if self.slug:
			self.parameters["slug"] = self.slug
		# -------------------

		try:
			self.get_response()
			logger.debug("URL='{}'".format(self.request.url))
		except requests.exceptions.HTTPError:
			logger.debug("Post response code: {}".format(self.response.status_code))
			if self.response.status_code == 400: # bad request
				logger.debug("URL={}".format(self.response.url))
				raise exc.BadRequest("400: Bad request. Error: \n{0}".format(json.dumps(self.response.json(), indent=4)))
			elif self.response.status_code == 404: # not found
				return None

		links_data = self.response.json()
		
		if isinstance(links_data, dict):
			# only one object was returned; make it a list
			links_data = [links_data]
		
		links = list()
		for d in links_data:
			link = ResourceLink(api=self.api)
			link.json = d
			
			link.s.id = d["id"]
			link.s.date = d["date"]
			link.s.date_gmt = d["date_gmt"]
			link.s.guid = d["guid"]
			link.s.modified = d["modified"]
			link.s.modified_gmt = d["modified_gmt"]
			link.s.slug = d["slug"]
			link.s.status = d["status"]
			link.s.type = d["type"]
			link.s.link = d["link"]
			link.s.title = d["title"]
			link.s.content = d["content"]
			link.s.template = d["template"]
			link.s.resource_url = d["resource_url"]
			link.s.resource_blurb = d["resource_blurb"]
			link.s.resource_name = d["resource_name"]
			link.s.category = d["category"]
			link.s.resource_author = d["resource_author"]
			link.s.resource_image = d["resource_image"]
		
			links.append(link)
			
		return links

	
	@property
	def slugs(self):
		'''
		The list of post slugs to retrieve.
		'''
		return self._slugs
		
	@slugs.setter
	def slugs(self, values):
		if values is None:
			self.parameters.pop("slugs", None)
			self._slugs = list()
			return
		elif not isinstance(values, list):
			raise ValueError("Slugs must be provided as a list (or append to the existing list).")
		
		for s in values:
			if isinstance(s, str):
				self._slugs.append(s)
			else:
				raise ValueError("Unexpected type for property list 'slugs'; expected str, got '{0}'".format(type(s)))

	@property
	def categories(self):
		return self._category_ids

	@categories.setter
	def categories(self, values):
		'''
		This method validates the categories passed to this request.
		
		It accepts category ID (integer or string) or the slug value.
		'''
		if values is None:
			self.parameters.pop("categories", None)
			self._category_ids = list()
			return
		elif not isinstance(values, list):
			raise ValueError("Categories must be provided as a list (or append to the existing list).")
		
		for c in values:
			cat_id = None
			if isinstance(c, Category):
				cat_id = c.s.id
#				self._category_ids.append(str(c.s.id))
			elif isinstance(c, int):
#				self._category_ids.append(str(c))
				cat_id = c
			elif isinstance(c, str):
				try:
					# is this a category ID value?
					cat_id = int(c)
					#self._category_ids.append(str(int(c)))
				except ValueError:
					# not a category ID value, try by slug?
					try:
						category = self.api.category(slug=c)
						cat_id = category.s.id
						#self._category_ids.append(category.s.id)
					except exc.NoEntityFound:
						logger.debug("Asked to find a category with the slug '{0}' but not found.".format(slug))
			
			# Categories are stored as string ID values.
			#
			self._category_ids.append(str(cat_id))
