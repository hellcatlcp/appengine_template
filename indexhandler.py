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
import jinja2
import main

from apiclient.discovery import build
from google.appengine.api import memcache

class IndexHandler(webapp2.RequestHandler):

  def get(self):
  	template = main.jinja_environment.get_template("index.html")
	self.response.out.write(template.render({}))
    


