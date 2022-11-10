import requests
import json


api_key = "8w3irUQRqrtNZixGrUdZXQKjAC8CYJOa"


#function to find the id for a location
def search_location(location):
    #base url for searching by location
    base_search_url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey="

    #format the location for the url
    location = location.replace(" ", "%20")

    query = "&q=" + location

    full_url = base_search_url + api_key + query

    #request data from api
    response = requests.get(full_url)

    #check that search yielded results#
    if response.text=="[]":
        return False
    else:
        #convert response into a json object
        data = json.loads(response.text)

        #return the location id for the api and the location's name
        return (data[0]["Key"], data[0]["LocalizedName"])



#function to check the forcast for a given location
def search_forecast(location_id, loc_name):
    #base url for finding a one day forecast
    base_search_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"

    #concatenate the base url to the location id and the api key
    full_url = base_search_url + location_id + "?apikey=" + api_key + "&details=true&metric=true"

    response = requests.get(full_url)

    forecast_data = json.loads(response.text)

    #store the required data as variables
    low_temp = round(forecast_data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"], 0)
    high_temp = round(forecast_data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"], 0)
    low_feels = forecast_data["DailyForecasts"][0]["RealFeelTemperature"]["Minimum"]["Phrase"]
    high_feels = forecast_data["DailyForecasts"][0]["RealFeelTemperature"]["Maximum"]["Phrase"]
    day_desc = forecast_data["DailyForecasts"][0]["Day"]["LongPhrase"]
    night_desc = forecast_data["DailyForecasts"][0]["Night"]["LongPhrase"]


    #concatenate this data to create a weather report for the day
    weather_report = "Expect " + day_desc + " weather today in " + loc_name + " and a " + night_desc + " night."
    weather_report += " There will be " + high_feels + " highs of " + str(high_temp) + " degrees and " + low_feels + " lows of " + str(low_temp)

    return weather_report


def get_forecast_report(location_name):
    #generate the results from the autocomplete search
    location_search_results = search_location(location_name)

    #check that search was successful before progressing
    if location_search_results:
        loc_id, loc_name = location_search_results
        return search_forecast(loc_id, loc_name)
    else:
        return "Error: Something went wrong with the search"








