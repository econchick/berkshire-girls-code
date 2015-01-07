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
    'client_id': 'f5ba18a10b1f4b02b18d261c534429f9',
    'client_secret': 'ef76a471ba624ab8b7d1c7b03916d6d4',
    'redirect_uri': DEPLOY_URL + 'callback',
    'token_url': 'https://accounts.spotify.com/api/token',
    'authorize_url': 'https://accounts.spotify.com/authorize'
}

OUTPUT_FILEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

OUTPUT_FILENAME = os.path.join(OUTPUT_FILEDIR, '/playlist_data.json')
