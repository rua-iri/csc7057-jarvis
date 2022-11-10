import requests
import json
from random import choice as random_choice
import pychromecast
from pychromecast.controllers.youtube import YouTubeController


#this function uses the api from invidious, an open source youtube front end, to select a random video from a youtube playlist
def get_video_from_playlist(list_code):

    #select a working mirror with an api from the list
    mirror_response = requests.get("https://api.invidious.io/instances.json?pretty=1&sort_by=api")
    mirror_data = json.loads(mirror_response.text)
    mirror_url = ""

    #select the first matching mirror
    for mirror in mirror_data:
        if mirror[1]["api"]==True:
            mirror_url = mirror[1]["uri"]
            break

    #use that mirror's api to get a list of all the videos in the playlist
    playlist_response = requests.get(mirror_url + "/api/v1/playlists/" + list_code)
    playlist_data = json.loads(playlist_response.text)
    videos_list = playlist_data["videos"]

    #return the playlist code for a random video
    rand_video = random_choice(videos_list)
    return rand_video["videoId"]


#function to cast a video to a chromecast
def cast_to_device(device_name, video_code):
    #scan for chromecasts with the same name
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[device_name])
    my_chromecast = chromecasts[0]
    my_chromecast.wait()

    chromecast_yt = YouTubeController()
    my_chromecast.register_handler(chromecast_yt)
    chromecast_yt.play_video(video_code)

    browser.stop_discovery()
