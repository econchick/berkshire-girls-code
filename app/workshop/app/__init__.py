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


from spotify import get_spotify_oauth_token
# General OAuth Setup
client_id = app.config.get("OAUTH").get('client_id')
client_secret = app.config.get("OAUTH").get('client_secret')
token_url = app.config.get("OAUTH").get('token_url')

app.logger.debug("Getting OAuth Token")
access_token = get_spotify_oauth_token(client_id, client_secret, token_url)
app.logger.debug("OAuth Token Received")
app.config["access_token"] = access_token

import website  # NOQA
