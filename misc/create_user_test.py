#!/usr/bin/env python

import os
from requests.auth import HTTPBasicAuth

import wordpress_orm
from wordpress_orm.entities import User

wordpress_api = wordpress_orm.API(url='http://content.sorghumbase.org/wordpress/index.php/wp-json/wp/v2/')
wordpress_api.authenticator = HTTPBasicAuth(os.environ['SB_WP_USERNAME'], os.environ['SB_WP_PASSWORD'])

user = User(api=wordpress_api)
user.s.username = "xxx_api_xxx"
user.s.first_name = "first name"
user.s.last_name = "last name"
user.s.password = "abc123"
user.s.email = "user@email.com"

response = user.commit()

print(response)
