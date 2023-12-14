import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os

TEQUILA_URL = 'https://api.tequila.kiwi.com'

load_dotenv()


class FlightSearch:

    def get_destination_code(self, city_name):
        location_url = f"{TEQUILA_URL}/locations/query"
        headers = {
            "apikey": os.getenv('TEQUILA_API_KEY')
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(location_url, headers=headers, params=query)
        code = response.json()['locations'][0]['code']
        return code

    def check_flights(self, departure_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": os.getenv('TEQUILA_API_KEY')
        }
        query = {
            "fly_from": departure_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
        }

        response = requests.get(f"{TEQUILA_URL}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            departure_city=data['cityFrom'],
            departure_airport=data['route'][0]['flyFrom'],
            destination_city=data['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            departure_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][-1]['local_departure'].split("T")[0]

        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data


