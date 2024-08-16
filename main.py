# main.py

from musics import MUSICS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# writeJson

def writeJson(jsonFile):
    with open("myjson1.json", "w") as f:
        json.dump(jsonFile, f, indent = 4)

##### Spotify Playlist Building
# authentitcating the spotify through the library. 


SCOPE = "playlist-modify-private"
USERNAME = "HelloKidusME"
CLIENT_ID = "7cd30832615c4a17967778d1849cc75c"
CLIENT_SECRET = "abe76dc280d343bb9e4784b4e1b8871e"
REDIRECTING_URL = "https://github.com/ktessma21"

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECTING_URL,scope=scope))

userID = sp.me()["id"]

# create a playlist
# sp.user_playlist_create(userID, "top 100 musics in 2024-05-12")
# DONE

# find the playlist ID
playlistID = sp.current_user_playlists()["items"][0]["id"]

# find the URIs/URLs of each music 

trackURIS = []
for music in MUSICS:
    track  = sp.search(q=music)
    trackURI = track["tracks"]["items"][0]["uri"]
    trackURIS.append(trackURI)

# writeJson(trackURI)

sp.playlist_add_items(playlist_id=playlistID, items=trackURIS, position=None)

