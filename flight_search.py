import requests 

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    endpoint = "https://api.tequila.kiwi.com/v2/search"

    authorization_header = {
        "Authorization": ""
    }

    params = {
        "apikey": "AP0yzH3RH3HUBhkt8TfjgPZHGdPNZ7X0",
        "fly_from": "SNA",
        "fly_to": "SFO",
        "date_from": "09/09/2023",
        "date_to": "03/09/2023"

    }

    response = requests.post(url=endpoint, headers=params)
    result = response.json()

    print(result)
