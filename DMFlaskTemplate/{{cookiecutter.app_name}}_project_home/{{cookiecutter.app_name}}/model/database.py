#!/usr/bin/python

''' This file handles a database connection. It can simply be deleted if not needed.
	
	The example given is for a PostgreSQL database, but can be modified for any other.
'''

import psycopg2

from flask import current_app as app, g
from sqlalchemy.orm import sessionmaker, scoped_session

from .DatabaseConnection import DatabaseConnection
from ..designpatterns import singleton

@singleton
class Database(object):
	
	def __init__(self):
		self.pool = None
		self.database_connection_string = None # can be set manually
		self._Session = None
		self.db_config = {}
		self.db = None # set in method "connect" below
		
	def connect(self, flask_app):
		''' Connect to database using connection parameters in flask_app.config. '''
	
		# create database connection string
		#
		if self.database_connection_string is None:
			# read details from configuration
			try:
				# the password is basically hard-coded at the moment - change as needed
				#with app.app_context():
			    self.db_config["host"]     = flask_app.config["DB_HOST"]
			    self.db_config["database"] = flask_app.config["DB_DATABASE"]
			    self.db_config["user"]     = flask_app.config["DB_USER"]
			    self.db_config["password"] = '' # set to empty string to force retrieval from ~/.pgpass
			    self.db_config["port"]     = flask_app.config["DB_PORT"]
			except KeyError:
			    current_app.logger.debug("ERROR: an expected key in the server configuration " + \
									     "file was not found.")
	
			self.database_connection_string = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(**self.db_config)
		
		# connect to database:
		self.db = DatabaseConnection(database_connection_string=self.database_connection_string)

	def pool(self, release):
		# NOTE: NOT IMPLEMENTED YET
		''' Return the pool of database connections for the database connected. '''
	
		# -----------------------------------
		# Database connection setup & methods
		# -----------------------------------
		# Ref: http://initd.org/psycopg/docs/module.html
		# Ref: http://packages.python.org/psycopg2/pool.html#module-psycopg2.pool
		# dsn = data source name
		
		if self.pool is None:
			
			db_info = {}
			#for key in self.config.options(""):
			#	db_info[key] = config.
		
		return self.pool
		
	def Session(self):
		''' Returns the SQLAlchemy Session base class. '''
		if self._Session is None:
			self._Session = scoped_session(sessionmaker(bind=self.db.engine, autocommit=False, autoflush=True))
		return self._Session
	
	def get_session(self):
		''' Place a new Session instance on the thread local global context "g". '''
		g.my_session = self.Session()
		return g.my_session

	
	### etc. ###
	
	## TODO: create a sample db file for PostgreSQL, SQLite, and SQLAlchemy