#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

import os

from .base import *

SECRET_KEY = ''
DEBUG = True
DEPLOY_URL = "http://localhost:5000/"
LOGGING = "DEBUG"
LOGGING_OUTPUT = "berkshires_girls_code.log"

OAUTH = {
    'client_id': '',
    'client_secret': '',
    'redirect_uri': DEPLOY_URL + 'callback',
    'token_url': 'https://accounts.spotify.com/api/token',
    'authorize_url': 'https://accounts.spotify.com/authorize'
}

OUTPUT_FILEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

OUTPUT_FILENAME = os.path.join(OUTPUT_FILEDIR, '/playlist_data.json')
