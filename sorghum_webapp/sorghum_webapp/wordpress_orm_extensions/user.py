'''

WordPress API reference: https://developer.wordpress.org/rest-api/reference/posts/
'''

import logging
import requests

from wordpress_orm import WPEntity, WPRequest, WPORMCacheObjectNotFoundError

logger = logging.getLogger("wordpress_orm")

class User(WPEntity):

	def __init__(self, id=None, session=None, api=None):
		super().__init__(api=api)

		# parameters that undergo validation, i.e. need custom setter
		self._context = None

		# cache related objects
		self._posts = None

	@property
	def schema_fields(self):
		return ["id", "username", "name", "first_name", "last_name", "email", "url",
			   "description", "link", "locale", "nickname", "slug", "registered_date",
			   "roles", "password", "capabilities", "extra_capabilities", "avatar_urls", "meta", "job_title"]

	@property
	def posts(self):
		if self._posts is None:
			pr = self.api.PostRequest()
			pr.author = self
			self._posts = pr.get()
		return self._posts

	def __repr__(self):
		return "<WP {0} object at {1}, id={2}, name='{3}'>".format(self.__class__.__name__, hex(id(self)), self.s.id, self.s.name)

	def gravatar_url(self, size=200, rating='g', default_image_style="mm"):
		'''
		Returns a URL to the Gravatar image associated with the user's email address.

		Ref: https://en.gravatar.com/site/implement/images/

		size: int, can be anything from 1 to 2048 px
		rating: str, maximum rating of the image, one of ['g', 'pg', 'r', 'x']
		default_image: str, type of image if gravatar image doesn't exist, one of ['404', 'mm', 'identicon', 'monsterid', 'wavatar', 'retro', 'robohash', 'blank']
		'''
		if rating not in ['g', 'pg', 'r', 'x']:
			raise ValueError("The gravatar max rating must be one of ['g', 'pg', 'r', 'x'].")

		if default_image_style not in ['404', 'mm', 'identicon', 'monsterid', 'wavatar', 'retro', 'robohash', 'blank']:
			raise ValueError("The gravatar default image style must be one of ['404', 'mm', 'identicon', 'monsterid', 'wavatar', 'retro', 'robohash', 'blank'].")

		if not isinstance(size, int):
			try:
				size = int(size)
			except ValueError:
				raise ValueError("The size parameter must be an integer value between 1 and 2048.")

		if isinstance(size, int):
			if 1 <= size <= 2048:
				#
				# self.s.avatar_urls is a dictionary with key=size and value=URL.
				# Sizes are predetermined, but not documented. Values found were ['24', '48', '96'].
				#
				grav_urls_dict = self.s.avatar_urls
				grav_url = grav_urls_dict[list(grav_urls_dict)[0]] # get any URL (we'll set our own size) / list(d) returns list of dictionary's keys
				grav_url_base = grav_url.split("?")[0]
				params = list()
				params.append("d={0}".format(default_image_style)) # set default image to 'mystery man'
				params.append("r={0}".format(rating)) # set max rating to 'g'
				params.append("s={0}".format(size))

				return "{0}?{1}".format(grav_url_base, "&".join(params))
		else:
			raise ValueError("The size parameter must be an integer.")

	@property
	def fullname(self):
		return "{0} {1}".format(self.s.first_name, self.s.last_name)


class UserRequest(WPRequest):
	'''

	'''
	def __init__(self, api=None):
		super().__init__(api=api)
		self.id = None # WordPress ID
		self._slugs = list() # can accept more than one

	@property
	def parameter_names(self):
		return ["context", "page", "per_page", "search", "exclude",
				"include", "offset", "order", "orderby", "slug", "roles"]

	@property
	def slug(self):
		return self._slugs

	@slug.setter
	def slug(self, value):
		if value is None:
			self._slugs = list()
		elif isinstance(value, str):
			self._slugs.append(value)
		elif isinstance(value, list):
			# validate data type
			for v in value:
				if not isinstance(v, str):
					raise ValueError("slugs must be string type; found '{0}'".format(type(v)))
			self._slugs = value

	def get(self):
		'''
		'''
		self.url = self.api.base_url + 'users'

		if self.id:
			self.url += "/{}".format(self.id)

		# -------------------
		# populate parameters
		# -------------------
		if self.context:
			self.parameters["context"] = self.context
			request_context = self.context
		else:
			request_context = "view" # default value

		if len(self.slug) > 1:
			self.parameters["slug"] = ",".join(self.slug)

		if self.search:
			self.parameters["search"] = self.search

		# -------------------

		try:
			self.get_response()
			logger.debug("URL='{}'".format(self.request.url))
		except requests.exceptions.HTTPError:
			logger.debug("User response code: {}".format(self.response.status_code))
			if self.response.status_code == 404:
				return None
			elif self.response.status_code == 404:
				return None

		users_data = self.response.json()

		if isinstance(users_data, dict):
			# only one object was returned; make it a list
			users_data = [users_data]

		users = list()
		for d in users_data:

			# Before we continue, do we have this User in the cache already?
			try:
				user = self.api.wordpress_object_cache.get(class_name=User.__name__, key=d["id"])
				users.append(user)
				continue
			except WPORMCacheObjectNotFoundError:
				pass

			user = User(api=self.api)
			user.json = d

			# Properties applicable to 'view', 'edit', 'embed' query contexts
			#
			#   "id", "name", "url", "description", "link", "slug", "avatar_urls"
			#
			user.s.id = d["id"]
			user.s.name = d["name"]
			user.s.url = d["url"]
			user.s.description = d["description"]
			user.s.link = d["link"]
			user.s.slug = d["slug"]
			user.s.avatar_urls = d["avatar_urls"]
			user.s.job_title = d["job_title"]

			# Properties applicable to only 'view', 'edit' query contexts:
			#
			if request_context in ["view", "edit"]:
				user.meta = d["meta"]

			# Properties applicable to only 'edit' query contexts
			#
			if request_context in ["edit"]:
				user.s.username = d["username"]
				user.s.first_name = d["first_name"]
				user.s.last_name = d["last_name"]
				user.s.email = d["email"]
				user.s.locale = d["locale"]
				user.s.nickname = d["nickname"]
				user.s.registered_date = d["registered_date"]
				user.s.roles = d["roles"]
				user.s.capabilities = d["capabilities"]
				user.s.extra_capabilities = d["extra_capabilities"]

			# add to cache
			self.api.wordpress_object_cache.set(class_name=User.__name__, key=str(user.s.id), value=user)
			self.api.wordpress_object_cache.set(class_name=User.__name__, key=user.s.slug, value=user)

			users.append(user)

		return users

	@property
	def context(self):
		return self._context

	@context.setter
	def context(self, value):
		if value is None:
			self._context = None
			return
		else:
			try:
				value = value.lower()
				if value in ["view", "embed", "edit"]:
					self._context = value
					return
			except:
				pass
		raise ValueError ("'context' may only be one of ['view', 'embed', 'edit'] ('{0}' given)".format(value))
