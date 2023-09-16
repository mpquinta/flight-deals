#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
from flight_search import FlightSearch
import notification_manager
from pprint import pprint

google_sheet_data = data_manager.DataManager()
sheet_data = google_sheet_data.prices
twilio = notification_manager.NotificationManager()

city = FlightSearch()

for i in range(len(sheet_data["prices"])):
    current_city = sheet_data["prices"][i]["city"]
    if sheet_data["prices"][i]["iataCode"] == '':
        iata_code = city.search_iata_code(current_city)
        google_sheet_data.update_iata_code(sheet_data["prices"][i]["id"], iata_code)

    # pass the cities into city.flight_search
    flight_search_results = city.flight_search(sheet_data["prices"][i]["iataCode"])
    pprint(flight_search_results)
    from_city = flight_search_results["data"][0]["route"][0]["cityFrom"]
    from_iata = flight_search_results["data"][0]["route"][0]["flyFrom"]
    to_city = flight_search_results["data"][0]["route"][0]["cityTo"]
    to_iata = flight_search_results["data"][0]["route"][0]["flyTo"]

    # print the cheapest price tickets
    flight_price = flight_search_results["data"][0]["price"]
    # print(f"{current_city}: ${flight_price}")

    # check cheapest flight against price in google sheet
    desired_price = sheet_data["prices"][i]["lowestPrice"]
    if flight_price < desired_price:
        twilio.send_text(flight_price, )
    # if price is cheaper than google sheet
        #send a text


