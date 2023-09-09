import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    end_point = "https://api.sheety.co/e8fbf885f6ddb9e986be03619cb06931/flightDeals/prices"

    get_response = requests.get(url=end_point)
    prices = get_response.json()
    # pprint(prices)
    
    def update_iata_code(self, row_id, iata_code):
        put_endpoint = f"https://api.sheety.co/e8fbf885f6ddb9e986be03619cb06931/flightDeals/prices/{row_id}"
        
        params = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(url=put_endpoint, json=params)