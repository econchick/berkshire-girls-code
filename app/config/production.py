#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

from .base import *

# SECRET_KEY should be in an env var defined on the system
SECRET_KEY = ''
DEBUG = False
TESTING = False
DEPLOY_URL = "https://berkshire-girls-code.herokuapp.com"
PREFERRED_URL_SCHEME = 'https'
LOGGING = "INFO"

# OAUTH client_secret should be in an env var defined on the system
OAUTH = {
    'client_id': '',
    'client_secret': '',
    'redirect_uri': DEPLOY_URL + '/callback',
    'token_url': 'https://accounts.spotify.com/api/token',
    'authorize_url': 'https://accounts.spotify.com/authorize'
}
