
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
		
		# add storage for custom fields
		self._job_title = None
	
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
	
	def postprocess_response(self):
		'''
		Process response after superclass handles it.
		'''
		#print(self.json)
		self.job_title = self.json['job_title']
		
