#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This script is used to launch myapplication.

Application initialization should go here.

'''

from flask import Flask

from myapplication import app # the app is created here
from myapplication.config import AppConfig
from myapplication.controllers import * # register the controllers with Flask
from myapplication.model import * # register any model (e.g. database) classes

config = AppConfig() # get access to configuration information

# register Flask modules (if any) here
#app.register_module(xxx)

app.run(debug=config.debugMode)


