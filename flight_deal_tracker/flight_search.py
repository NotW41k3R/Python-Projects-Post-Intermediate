from dotenv import load_dotenv
import requests
import os

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.key = os.getenv("AMADEUS_API_KEY")
        self.secret = os.getenv("AMADEUS_API_SECRET")
        if not self.key or not self.secret:
            raise ValueError("Missing Amadeus API credentials")
        self.auth_token=self.get_auth_token()
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }

    def get_auth_token(self):
        auth_url="https://test.api.amadeus.com/v1/security/oauth2/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.key,
            "client_secret": self.secret,
        }
        response = requests.post(url=auth_url, data=payload)
        response.raise_for_status()
        return response.json()['access_token']
    
    def get_iata(self, city_name):
        url="https://test.api.amadeus.com/v1/reference-data/locations/cities"
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=url, params=query, headers=self.headers)
        response.raise_for_status()
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        url="https://test.api.amadeus.com/v2/shopping/flight-offers"
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=url,
            headers=self.headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()