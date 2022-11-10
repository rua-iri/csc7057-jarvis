import requests
import json

def searchforterm(term):
    #the base url for the api
    url = "https://duckduckgo-duckduckgo-zero-click-info.p.rapidapi.com/"

    #the query which will be searched
    queryName = term

    querystring = {"q": queryName,"callback":"process_duckduckgo","no_html":"1","no_redirect":"1","skip_disambig":"1","format":"json"}

    #include the api key in the headers
    headers = {
        "X-RapidAPI-Key": "da6d853f99msh84e969b524c8f46p161095jsn0f0df9022e87",
        "X-RapidAPI-Host": "duckduckgo-duckduckgo-zero-click-info.p.rapidapi.com"
    }

    #request the page
    response = requests.request("GET", url, headers=headers, params=querystring)

    #format the response and load it as a json object
    searchdata = json.loads(response.text[19:-2])

    #extract the key information from the json
    search_results = searchdata["Abstract"]

    #only return the abstract if there is any text there
    if search_results!="":
        return search_results
    else:
        return "No results found for: " + term
