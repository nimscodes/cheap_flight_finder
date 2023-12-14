import requests
from pprint import pprint

SHEET_URL = 'https://api.sheety.co/dedef4127d0c13812f19ece2d08cffe1/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_URL)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self, code, id):
        new_data = {
            "price": {
                "iataCode": code,
            }
        }
        response = requests.put(f"{SHEET_URL}/{id}", json=new_data)
        print(response.text)

    def update_price(self, new_price, id):
        new_data = {
            "price": {
                "lowestPrice": new_price,
            }
        }
        response = requests.put(f"{SHEET_URL}/{id}", json=new_data)
        print(response.text)

