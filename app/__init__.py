#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

import logging
from logging import Formatter
import os

from flask import Flask


tpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__, template_folder=tpl_dir, static_folder=static_dir)


# Flask-specific configuration
app.config.from_object('app.config.local')

DEBUG = app.config['DEBUG']


# Logging setup
if not DEBUG:
    from logging.handlers import RotatingFileHandler
    output_file = app.config['LOGGING_OUTPUT']
    file_handler = RotatingFileHandler(output_file)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(app.config['LOGGING'])
    app.logger.addHandler(file_handler)

else:
    stream_handler = logging.StreamHandler()
    stream_formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(stream_formatter)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(app.config['LOGGING'])
    app.logger.addHandler(stream_handler)

import website  # NOQA

from oauth import GeneralSpotifyOAuth
# General OAuth Setup
oauth_client = GeneralSpotifyOAuth()
encoded_auth = oauth_client.get_encoded_auth()
headers, data = oauth_client.setup_basic_request(encoded_auth)

app.logger.debug("Getting OAuth Token")
access_token = oauth_client.get_oauth_token(headers, data)
app.logger.debug("OAuth Token Received")
app.config["access_token"] = access_token
