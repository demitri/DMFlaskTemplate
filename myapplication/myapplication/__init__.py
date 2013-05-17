#!/usr/bin/python

from flask import Flask

# creates the app instance using the name of the module
app = Flask(__name__)

print "{0}App '{1}' created.{2}".format('\033[92m', __name__, '\033[0m') # to remove later

# Perform early app setup here.
