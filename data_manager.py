import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    end_point = "https://api.sheety.co/e8fbf885f6ddb9e986be03619cb06931/flightDeals/prices"

    get_response = requests.get(url=end_point)
    prices = get_response.json()
    # pprint(prices)
    
    put_endpoint = "https://api.sheety.co/e8fbf885f6ddb9e986be03619cb06931/flightDeals/prices/[Object ID]"