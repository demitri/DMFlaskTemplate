
from wordpress_orm.entities import User

class SBUser(User):
	'''

	'''
	def __init__(self, api=None):
		'''

		'''
		super().__init__(api=api)

		# add custom fields
		self.add_schema_field("job_title")
		self.add_schema_field("organization")

		# add storage for custom fields
		self._job_title = None
		self._organization = None

	@property
	def job_title(self):
		return self._job_title

	@job_title.setter
	def job_title(self, new_title):
		'''

		'''
		if isinstance(new_title, str) is False:
			raise Exception("The property 'job_title' is expected to be a string.")
		self._job_title = new_title

	@property
	def organization(self):
		return self._organization

	@organization.setter
	def organization(self, new_organization):
		'''

		'''
		if isinstance(new_organization, str) is False:
			raise Exception("The property 'organization' is expected to be a string.")
		self._organization = new_organization

	def postprocess_response(self):
		'''
		Process response after superclass handles it.
		'''
		#print(self.json)
		self.job_title = self.json['job_title']
		self.organization = self.json['organization']
