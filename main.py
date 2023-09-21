#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

google_sheet_data = data_manager.DataManager()
sheet_data = google_sheet_data.prices
twilio = NotificationManager()

city = FlightSearch()

for i in range(len(sheet_data["prices"])):
    current_city = sheet_data["prices"][i]["city"]
    if sheet_data["prices"][i]["iataCode"] == '':
        iata_code = city.search_iata_code(current_city)
        google_sheet_data.update_iata_code(sheet_data["prices"][i]["id"], iata_code)

    # pass the cities into city.flight_search
    flight_search_results = city.flight_search(sheet_data["prices"][i]["iataCode"])
        # pprint(flight_search_results)
    try:       
        #extract necessary info from the flight search results 
        from_city = flight_search_results["data"][0]["route"][0]["cityFrom"]
        from_iata = flight_search_results["data"][0]["route"][0]["flyFrom"]
        to_city = flight_search_results["data"][0]["route"][0]["cityTo"]
        to_iata = flight_search_results["data"][0]["route"][0]["flyTo"]
        start_date_raw = flight_search_results["data"][0]["route"][0]["local_departure"].split("T")
        start_date = start_date_raw[0]
        end_date_raw = flight_search_results["data"][0]["route"][1]["local_departure"].split("T")
        end_date = end_date_raw[0]
        # print(from_city, from_iata, to_city, to_iata, start_date, end_date)

        # print the cheapest price tickets
        flight_price = flight_search_results["data"][0]["price"]
        # print(f"{current_city}: ${flight_price}")

        # check cheapest flight against price in google sheet
        desired_price = sheet_data["prices"][i]["lowestPrice"]
        
        # print("desired price: ", desired_price)
        if flight_price < desired_price:
            twilio.send_text(
                message=f"Low price alert! Only ${flight_price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata} from {start_date} to {end_date}.")
    
    except IndexError or TypeError:
        continue


