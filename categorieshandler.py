#!/usr/bin/env python
#
# Copyright 2012 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import httplib2
import logging
import os
import pickle
import webapp2

from apiclient.discovery import build
from oauth2client.appengine import oauth2decorator_from_clientsecrets
from oauth2client.client import AccessTokenRefreshError
from google.appengine.api import memcache
import main
import jinja2

class CategoriesHandler(webapp2.RequestHandler):

  def get(self):

  	guideCategories = main.service.guideCategories().list(
 		part="id,snippet", regionCode='GB'
	).execute()

	template = main.jinja_environment.get_template("categories.html")
	self.response.out.write(template.render(
		{'guideCategories': guideCategories}
	))
  
	

    
