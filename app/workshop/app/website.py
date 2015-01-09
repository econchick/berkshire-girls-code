#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

from flask import g, request, render_template

from app import app
import spotify as sp

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
        parsed_data, _ = sp.parse_track_data(track_data)

        # sort the parsed_data of tracks into their appropriate buckets
        app.logger.debug("Sorting track data")
        bucket_data = sp.sort_track_data(parsed_data)

        # create a bar chart with the bucket_data!
        return render_template("playlist.html", results=bucket_data)


#####
# TODO: The following function is what you will need to complete
####
@app.route('/word-cloud/', methods=["GET", "POST"])
def word_cloud():
    # If the request is just "GET", simply return the wordcloud.html template
    if request.method == "GET":
        return render_template("wordcloud.html")

    # If the user submits the form on wordcloud.html, it's then a "POST"
    # request.  Therefore, we must implement the POST logit
    if request.method == "POST":
        # Grab the username from the form that the user submitted with the
        # POST request

        # Grab the access token so we can authenticate our requests

        # Using the functions we implemented in spotify.py:
        # Get the playlist information using our access token and username

        # Then get the track URLs that make up those playlists

        # Request track information from those track URLs

        # Finally, parse the data associated with the tracks

        # Once that logic is all complete, return the same "wordcloud.html"
        # template, but with the context data "results" set to our word_data

        # DELETE "pass" once you've started implementing this part
        pass
