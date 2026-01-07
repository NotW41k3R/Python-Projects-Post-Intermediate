# Shetty
from flight_search import FlightSearch
from dotenv import load_dotenv
from pprint import pprint 
import requests
import os

username=os.getenv("SHETTY_USERNAME")
projectName=os.getenv("SHETTY_PROJECT_NAME")
sheetName=os.getenv("SHETTY_SHEET_NAME")

load_dotenv()

class DataManager:
    def __init__(self):
        self.flight_search=FlightSearch()
        self.base_url=f"https://api.sheety.co/{username}/{projectName}/{sheetName}"
        self.auth_token=os.getenv("SHETTY_TOKEN")
        self.headers={
            'Authorization': f'Bearer {self.auth_token}'
        }
        self.destination_data={}
    
    def get_destinations(self):
        response = requests.get(url=self.base_url,headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()['prices']
        return response.json()['prices']
    
    def fill_iata(self):
        cities = self.get_destinations()

        for city in cities:
            current_city = city['city']
            current_id = city['id']

            city_iata = self.flight_search.get_iata(current_city)
            payload = {
                'price': {
                    'city': f'{city['city']}',
                    'iataCode': f'{city_iata}',
                    'id': f'{city['id']}',
                    'lowestPrice': f'{city['lowestPrice']}',
                }
            }
            # response = requests.put(url=f"{self.base_url}/{current_id}", json=payload, headers=self.headers)
            # response.raise_for_status()
            print(f"Filled IATA for {current_city}")
        return self.get_destinations()
        
