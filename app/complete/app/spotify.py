#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Lynn Root

import base64
import datetime
import json
from operator import itemgetter

import requests


class SpotifyApiError(Exception):
    pass


# Get OAuth token
def get_spotify_oauth_token(client_id, client_secret, token_url):
    to_encode = client_id + ":" + client_secret
    encoded_auth = base64.b64encode(to_encode)
    headers = {"Authorization": "Basic %s" % encoded_auth}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url=token_url,
                             headers=headers,
                             data=data)

    if response.status_code == requests.codes.ok:
        return response.json()['access_token']
    else:
        response_error = json.loads(response.text).get('error')
        msg = "Error getting OAuth token: {e}".format(e=response_error)
        raise SpotifyApiError(msg)


# NOTE: the more "pythonic" way to do this is:
# >>> import dateutil.parser
# >>> foo = dateutil.parser.parse(raw_date)
# but I'd like to show some string slicing
def parse_raw_date(raw_date):
    # 2014-09-09T15:00:27Z
    if raw_date:
        year = int(raw_date[:4])
        month = int(raw_date[5:7])
        day = int(raw_date[8:10])
        return datetime.date(year, month, day)
    return datetime.date(2000, 01, 01)


def parse_track_data(track_data):
    parsed_track_data = []
    song_data = []
    for playlist in track_data:
        for track in playlist:
            ttrack = track.get('track')
            if ttrack:
                name = ttrack.get('name')
                added_at_raw = track.get('added_at')
                added_at = parse_raw_date(added_at_raw)
                parsed_track_data.append((name, added_at))

                artists = ttrack.get('artists')
                album = ttrack.get('album').get('name')
                href = ttrack.get('href')
                artist_names = [n.get('name') for n in artists]
                data = {
                    "album": album,
                    "href": href,
                    "artists": artist_names[0],
                    "name": name
                }
                song_data.append(data)
            else:
                continue

    parsed_track_data = sorted(parsed_track_data, key=itemgetter(1))
    return parsed_track_data, song_data


def create_buckets(beg_date, end_date):
    buckets = [beg_date]

    bucket = beg_date
    while bucket < end_date:
        year, month = divmod(bucket.month + 1, 12)
        if month == 0:
            month = 12
            year = year - 1
        bucket = datetime.date(bucket.year + year, month, 1)
        buckets.append(bucket)

    return buckets


def sort_track_data(track_data):
    # returns {'2011-01': 5, '2011-02': 0, '2011-03': 4}
    cumulated_data = []
    beginning_date = track_data[0][1]
    ending_date = track_data[-1][1]

    buckets = create_buckets(beginning_date, ending_date)

    for b in buckets:
        data = {}
        bucket = b.strftime("%Y-%m")
        counter = 0
        for t in track_data:
            if t[1].year == b.year and t[1].month == b.month:
                counter += 1
        data["month"] = bucket
        data["value"] = counter
        cumulated_data.append(data)

    return cumulated_data


#####
# The following functions are what you should have implemented
#####

# Implement the function to get a user's playlists
def get_user_playlists(token, username):
    # NOTE: this function takes two arguments: token, and username

    # Construct a dictionary that contains authorization headers
    headers = {"Authorization": "Bearer %s" % token}

    # Create a string for the URL that we will make a request to
    playlist_url = "https://api.spotify.com/v1/users/{0}/playlists".format(
        username)

    # Send a GET request to the URL we previously defined with the header
    # dictionary we also previously defined
    response = requests.get(url=playlist_url, headers=headers)

    # To be good coders, we should handle if anything went wrong when we
    # sent that request to the URL

    # If the response was ok, then return the JSON data of the response
    if response.status_code == requests.codes.ok:
        return response.json()

    # Otherwise, we must have gotten an error, so let's return an error
    # message through Python's "raise"
    else:
        response_error = json.loads(response.text).get('error')
        msg = "Error getting {0}'s playlists: {1}".format(username,
                                                          response_error)
        raise SpotifyApiError(msg)


# Implement the function to get tracks URLs of the user's playlists
def get_playlist_track_urls(playlists, username):
    # NOTE: this function takes two arguments: playlists (which will be the
    # JSON data returned from get_user_playlists function), and the username

    # Construct an empty list so we can add to it
    track_urls = []

    # Grab the 'items' element of the previously returned JSON
    items = playlists.get('items')

    # Let's iterate over each item, and only add playlist items whose owner
    # is the same as the current user (the user could otherwise just be
    # following someone else's playlist)
    for item in items:
        # Skip over any playlists the user doesn't actuall own
        if item.get('owner').get('id') != username:
            continue
        # Otherwise,
        else:
            # First get 'tracks' from the item
            tracks = item.get('tracks')
            # Then get the 'href' or the url of the particular track
            tracks_url = tracks.get('href')
            # And add it to our empty list
            track_urls.append(tracks_url)

    # After we're finished iterating over each item, return the list of
    # track URLs
    return track_urls


# Implement the function to request track data from the user's playlists
def get_tracks(track_urls, token):
    # NOTE: This function will take in two arguments: the track URLs
    # returned from get_playlist_track_urls, and the token

    # Construct a dictionary that contains authorization headers
    headers = {"Authorization": "Bearer {t}".format(t=token)}

    # Construct an empty list so we can add to it
    track_data = []

    # Iterate over each of the URLs we got earlier
    for url in track_urls:
        # For each URL, send a GET request to the URL with the header
        # dictionary that we defined earlier
        response = requests.get(url=url, headers=headers)

        # If the response to the request was OK, then:
        if response.status_code == requests.codes.ok:
            # Grab the values of the "items" key from the JSON response
            items = response.json().get('items')
            # Then add all that data of the track to our list
            track_data.append(items)

    # After we're finished iterating over each item, return the list
    # of track data
    return track_data
