import requests
import smtplib
import os

my_email=os.environ.get("EMAIL")
my_password=os.environ.get("PASSWORD")
api_key = os.environ.get("OWN_API_KEY")

parameters={
    "lat" : 36.740379,
    "lon" : -88.635899,
    "appid" : api_key,
    "cnt" : 4
}
url="https://api.openweathermap.org/data/2.5/forecast"

def will_rain(weather_id_list):
    for wid in weather_id_list:
        if wid < 700:
            return True
    return False

response = requests.get(url, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_list = weather_data["list"]
weather_id_list=[]

for hr_data in weather_list:
    weather_id = hr_data["weather"][0]['id']
    weather_id_list.append(weather_id)

if will_rain(weather_id_list):
    message = "It will rain"
else:
    message = "It will rain't"

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: Rain Notifier\n\n{message}")
