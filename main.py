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

"""Starting template for Google App Engine applications.

Use this project as a starting point if you are just beginning to build a Google
App Engine project. Remember to download the OAuth 2.0 client secrets which can
be obtained from the Developer Console <https://code.google.com/apis/console/>
and save them as 'client_secrets.json' in the project directory.
"""

import httplib2
import logging
import os
import pickle
import webapp2
import jinja2

from indexhandler import IndexHandler
from categorieshandler import CategoriesHandler


from apiclient.discovery import build
from oauth2client.appengine import oauth2decorator_from_clientsecrets
from oauth2client.client import AccessTokenRefreshError
from google.appengine.api import memcache


# set up jinj templating enviroment
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret.
# You can see the Client ID and Client secret on the API Access tab on the
# Google APIs Console <https://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Helpful message to display in the browser if the CLIENT_SECRETS file
# is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
<h1>Warning: Please configure OAuth 2.0</h1>
<p>
To make this sample run you will need to populate the client_secrets.json file
found at:
</p>
<code>%s</code>
<p>You can find the Client ID and Client secret values
on the API Access tab in the <a
href="https://code.google.com/apis/console">APIs Console</a>.
</p>

""" % CLIENT_SECRETS


http = httplib2.Http(memcache)
service = build("youtube", "v3", http=http, developerKey="INSERTZ_KEYZ_ERE")  


# Set up an OAuth2Decorator object to be used for authentication.  Add one or
# more of the following scopes in the scopes parameter below. PLEASE ONLY ADD
# THE SCOPES YOU NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
decorator = oauth2decorator_from_clientsecrets(
    CLIENT_SECRETS,
    scope=[
      'https://www.googleapis.com/auth/youtube.readonly',
      'https://www.googleapis.com/auth/youtube',
      'https://www.googleapis.com/auth/youtubepartner',
      'https://www.googleapis.com/auth/youtube.upload',
    ],
    message=MISSING_CLIENT_SECRETS_MESSAGE)


application = webapp2.WSGIApplication(
  [
    ('/', IndexHandler),
    (decorator.callback_path, decorator.callback_handler()),

    ('/categories', CategoriesHandler)
    ],
  debug=True)