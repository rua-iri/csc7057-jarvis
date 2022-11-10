import requests
import json


def find_crypto_id(id_list, conversion_currency):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '3322909c-46dc-4d78-9895-ddaa5efea965',
    }

    parameters = {
      'start':'1',
      'limit':'5000',
      'symbol':id_list
    }

    response = requests.request("GET", url, headers=headers, params=parameters)

    #load the response as a json object
    data = json.loads(response.text)
    coin_ids = []

    #append all ids to a list
    for elem in data["data"]:
        coin_ids.append(elem["id"])

    #perform another query to get the id of the conversion currency id
    parameters = {
      'start':'1',
      'limit':'5000',
      'symbol':conversion_currency
    }

    response = requests.request("GET", url, headers=headers, params=parameters)
    data = json.loads(response.text)
    conversion_id = data["data"][0]["id"]


    return coin_ids, conversion_id


def get_crypto_price(id_list, convert_id):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '3322909c-46dc-4d78-9895-ddaa5efea965',
    }

    #convert the list to a string and format correctly
    id_string = str(id_list)[1:-1]
    id_string = id_string.replace(" ", "")

    parameters = {
        'id':id_string,
        'convert_id':convert_id
    }

    response = requests.request("GET", url, headers=headers, params=parameters)

    data = json.loads(response.text)

    #create an empty list for the currencies and their values
    crypto_values = []

    #loop through each currency
    for elem in data["data"]:
        crypto_name = data["data"][elem]["name"]
        #round the price to three decimal places
        crypto_price = round(data["data"][elem]["quote"][str(convert_id)]["price"], 3)

        if crypto_price>0:
            crypto_values.append(crypto_name + ":" + str(crypto_price))

    return crypto_values




def get_crypto_data(desired_conversion):
    #comma separated list of desired cryptocurrencies
    desired_cryptos = "BTC,ETH,XMR,DOGE"

    crypto_ids, convert_id = find_crypto_id(desired_cryptos, desired_conversion)

    value_list = get_crypto_price(crypto_ids, convert_id)

    return value_list
