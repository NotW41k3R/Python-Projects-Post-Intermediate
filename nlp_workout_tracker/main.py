import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

SHETTY_USERNAME = os.environ.get("SHETTY_USERNAME")
SHETTY_PROJECT_NAME = "myWorkouts" #Project name here
SHETTY_SHEETNAME = "workouts" #Sheet name here
SHETTY_TOKEN = os.environ.get("SHETTY_TOKEN")
today = dt.datetime.today()

headers= {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

shetty_headers = {
    'Authorization': f'Basic {SHETTY_TOKEN}'
}
base_url = "https://app.100daysofpython.dev"
post_url = f"{base_url}/v1/nutrition/natural/exercise"
query = input("What activity did you perform? ")

post_parameters ={
    "query": query                       # Required: Exercise description
    # "weight_kg": 70,                   # Optional: Weight in kg (1-500)
    # "height_cm": 175,                  # Optional: Height in cm (1-300)
    # "age": 30,                         # Optional: Age (1-150)
    # "gender": "male",                  # Optional: "male" or "female"
}

response = requests.post(url=post_url, json=post_parameters, headers=headers)
response.raise_for_status()

exercise_data = response.json()['exercises']
exercise_duration = exercise_data[0]['duration_min']
exercise_name = exercise_data[0]["name"].capitalize()
exercise_calories = exercise_data[0]['nf_calories']
print()

shetty_url = f"https://api.sheety.co/{SHETTY_USERNAME}/{SHETTY_PROJECT_NAME}/{SHETTY_SHEETNAME}"

shetty_row_data = {
    'workout': {
        'date' : today.date().strftime("%d/%m/%Y"),
        'time' : today.time().strftime("%H:%M:%S"),
        'exercise' : exercise_name,
        'duration' : exercise_duration,
        'calories' : exercise_calories
    }
}

response2 = requests.post(url=shetty_url, json=shetty_row_data, headers=shetty_headers)
response2.raise_for_status()

# Documentation : https://app.100daysofpython.dev/services/nutrition/docs