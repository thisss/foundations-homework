#!/usr/bin/env python3

# SEARCH ENGINE
# 
# Make a non-IPython Notebook that automates browsing for top tracks
# Prompts for an artist
# you put it in, displays the results, asks which one you want (numbered)
# you enter a number
# It displays their top tracks, then their MOST popular album and their least popular album. if they only have one album it says that they only have one album.

import requests

artist = input("What artist are you looking for? ")

# Get the data from spotify's api

response = requests.get('https://api.spotify.com/v1/search?query=' + artist + '&type=artist&country=CH&limit=50')
data = response.json()
artists = data['artists']['items']

# Find the right artist

if len(artists) > 1:
    print("I found more than one artist with this name.")
    counter = 1
    for option in artists:
        print(counter, option['name'])
        counter += 1
    artist_option = int(input("Please type in the matching number. "))
    artist_id = artists[artist_option - 1]['id']
    artist_name = artists[artist_option - 1]['name']
else:
    artist_id = artists[0]['id']
    artist_name = artist[0]['name']

# Get the details about the artist.

response1 = requests.get("https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks?country=US")
data1 = response1.json()
tracks = data1['tracks']
album_list = []
album_names = []

print("\n" + "These are the most popular tracks on Spotify by", artist_name + ":\n")
for track in tracks:
    print(track['name'], "(Popularity:", str(track['popularity']) + ')')

print("\n" + artist_name, "has the following albums on Spotify:\n")

counter = 0
for album in tracks: 
    album_list.append(data1['tracks'][counter]['album']['id'])
    album_names.append(data1['tracks'][counter]['album']['name'])
    counter += 1
album_list_short = set(album_list)
print(", ".join(set(album_names)))

# Get albums from Spotify

response2 = requests.get("https://api.spotify.com/v1/albums/?ids=" + ",".join(album_list_short))
data2 = response2.json()
albums = data2['albums']

pop_album = albums[0]
flop_album = albums[0]

# Calculate top and flop album.

for album in albums:
    if album['popularity'] > pop_album['popularity']:
        pop_album = album
    elif album['popularity'] < flop_album['popularity']:
        flop_album = album

if len(album_list_short) == 1:
    print(artist_name, "has only one album listed on Spotify:", albums[0]['name'] + ".")
else:
    print("The album \"" + pop_album['name'] + "\" is the most popular album of", artist_name, "on Spotify. \"" + flop_album['name'] + "\" is the least popular.")
