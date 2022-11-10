import requests
import json
import time

#program to generate a random joke
def gen_joke():
    j_url = "https://v2.jokeapi.dev/joke/Any?safe-mode&type=twopart"
    response = requests.get(j_url)

    data = json.loads(response.text)

    return [data["setup"], data["delivery"]]

