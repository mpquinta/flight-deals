#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
from flight_search import FlightSearch

google_sheet_data = data_manager.DataManager()
sheet_data = google_sheet_data.prices

for i in range(len(sheet_data["prices"])):
    if sheet_data["prices"][i]["iataCode"] == '':
        city = FlightSearch(city=sheet_data["prices"][i]["city"])
        sheet_data["prices"][i]["iataCode"] = city.iata_code

print(sheet_data)