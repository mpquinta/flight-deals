import requests 

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass
        # self.iata_code = "TESTING - this is coming from the FLIGHT SEARCH class!"

    def search_iata_code(self, city):
        query_endpoint = "https://api.tequila.kiwi.com/locations/query"

        headers = {
            "apikey": "AP0yzH3RH3HUBhkt8TfjgPZHGdPNZ7X0"
        }

        params = {
            "term": city
        }

        get_response = requests.get(url=query_endpoint, headers=headers, params=params)
        city_info = get_response.json()
        # print(city_info)

        return city_info["locations"][0]["code"]


        # endpoint = "https://api.tequila.kiwi.com/v2/search"

        # authorization_header = {
        #     "Authorization": ""
        # }

        # params = {
        #     "apikey": "AP0yzH3RH3HUBhkt8TfjgPZHGdPNZ7X0",
        #     "fly_from": "SNA",
        #     "fly_to": "SFO",
        #     "date_from": "09/09/2023",
        #     "date_to": "03/09/2023"

        # }

        # response = requests.post(url=endpoint, headers=params)
        # result = response.json()

        # print(result)
