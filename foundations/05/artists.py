#!/usr/bin/env python3

import requests

artist = input("What artist are you looking for? ")

# Get the data from spotify's api

response = requests.get('https://api.spotify.com/v1/search?query=' + artist + '&type=artist&country=CH&limit=50')
data = response.json()
artists = data['artists']['items']


# Find the right artist

if len(data['artists']) > 1:
    print("I found more than one artist with this name.")
    counter = 1
    for option in artists:
        print(counter, option['name'])
        counter += 1
    artist_option = int(input("Please type in the matching number."))
    artist_id = artists[artist_option]['id']
    artist_name = artists[artist_option]['name']
else:
    artist_id = artists[0]['id']
    artist_name = artist[0]['name']

# Get the details about the artist.

response1 = requests.get("https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks?country=CH")
data1 = response1.json()

tracks = data1['tracks']
album_list = []

print("These are the most popular tracks on Spotify by", artist_name + ":\n")
for track in tracks:
    print(track['name'], "(Popularity:", str(track['popularity']) + ')')

print(artist_name, "has the following albums on Spotify:\n")

for album in tracks: 
    album_list.append(data1['tracks'][0]['album']['name'])
print(set(album_list))
