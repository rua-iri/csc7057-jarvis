import requests
import json



def gen_fact():
    f_url = "https://api.api-ninjas.com/v1/facts?limit=1"
    f_response = requests.get(f_url, headers={"X-Api-Key":"VzxZ3YQ04NLvsgSymOKR9Q==2NQLyfXNHpiflBUm"})
    f_data = json.loads(f_response.text)
    return f_data[0]["fact"]

