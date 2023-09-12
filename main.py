#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
from flight_search import FlightSearch
from pprint import pprint

google_sheet_data = data_manager.DataManager()
sheet_data = google_sheet_data.prices

city = FlightSearch()

for i in range(len(sheet_data["prices"])):
    current_city = sheet_data["prices"][i]["city"]
    if sheet_data["prices"][i]["iataCode"] == '':
        iata_code = city.search_iata_code(current_city)
        google_sheet_data.update_iata_code(sheet_data["prices"][i]["id"], iata_code)

    # pass the cities into city.flight_search
    flight_search_results = city.flight_search(sheet_data["prices"][i]["iataCode"])
    # print(flight_search_results)
    flight_price = flight_search_results["data"][0]["price"]
    # print(flight_price)
    print(f"{current_city}: ${flight_price}")    