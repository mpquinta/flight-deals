import requests
from datetime import datetime, timedelta

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.headers = {
            "apikey": "AP0yzH3RH3HUBhkt8TfjgPZHGdPNZ7X0"
        }

    def search_iata_code(self, city):
        query_endpoint = "https://api.tequila.kiwi.com/locations/query"

        params = {
            "term": city
        }

        get_response = requests.get(url=query_endpoint, headers=self.headers, params=params)
        city_info = get_response.json()
        # print(city_info)

        return city_info["locations"][0]["code"]

    def flight_search(self, iata_code):
        search_endpoint = "https://api.tequila.kiwi.com/v2/search"

        params = {
            "fly_from": "SNA",
            "fly_to": iata_code,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=181)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=search_endpoint, headers=self.headers, params=params)
        result = response.json()

        return result

