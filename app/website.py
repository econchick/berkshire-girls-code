#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

from flask import g, request, render_template
from werkzeug.contrib.cache import SimpleCache

import spotify as sp

from app import app

cache = SimpleCache()

# TODO: if response is "access token expired"


@app.before_request
def before_request():
    g.name = app.config['MY_NAME']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/playlist/', methods=["GET", "POST"])
def playlist():
    if request.method == "GET":
        return render_template('playlist.html')

    if request.method == "POST":
        username = request.form.get('spotifyname')
        app.logger.debug("Username: {0}".format(username))

        # try to get from Cache first
        bucket_data = cache.get(username + "-bucket-data")
        if bucket_data is None:
            # get oauth access token
            access_token = app.config.get("access_token")
            # get the requested user's public playlists
            app.logger.debug("Getting {0}'s playlists.".format(username))
            playlists = sp.get_user_playlists(access_token, username)
            app.logger.debug("Received {0}'s playlists.".format(username))

            # parse out the tracks URL for each playlist
            app.logger.debug("Parsing track URLs")
            track_urls = sp.get_playlist_track_urls(playlists, username)
            app.logger.debug("Parsed track URLs")

            # request track data from the tracks URLs
            app.logger.debug("Getting tracks")
            track_data = sp.get_tracks(track_urls, access_token)

            # parse track data into parsed_data
            app.logger.debug("Parsing track data")
            parsed_data, artist_data = sp.parse_track_data(track_data)

            # sort the parsed_data of tracks into their appropriate buckets
            app.logger.debug("Sorting track data")
            bucket_data = sp.sort_track_data(parsed_data)

            cache.set(username + '-bucket-data', bucket_data, timeout=10 * 60)

        # create a bar chart with the bucket_data!
        return render_template("playlist.html", results=bucket_data)


@app.route('/word-cloud/', methods=["GET", "POST"])
def word_cloud():
    if request.method == "GET":
        return render_template("wordcloud.html")
    if request.method == "POST":
        username = request.form.get('spotifyname')
        word_data = cache.get(username + '-word-data')
        if word_data is None:
            access_token = app.config.get("access_token")

            playlists = sp.get_user_playlists(access_token, username)
            track_urls = sp.get_playlist_track_urls(playlists, username)

            track_data = sp.get_tracks(track_urls, access_token)
            parsed_data, word_data = sp.parse_track_data(track_data)
            cache.set(username + '-word-data', word_data, timeout=10 * 60)

        return render_template("wordcloud.html", results=word_data)
