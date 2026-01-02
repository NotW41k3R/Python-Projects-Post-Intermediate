import requests
from datetime import datetime
import smtplib
import os
import time

my_email=os.getenv("EMAIL")
my_password=os.getenv("PASSWORD")

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if(abs(MY_LAT-iss_latitude)<=5 and abs(MY_LONG-iss_longitude)<=5):
        return True
    else:
        return False

def is_after_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now>sunset or time_now<sunrise:
        return True
    else:
        return False
    
while True:
    time.sleep(60)
    if is_after_sunset() and iss_overhead():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject: ISS Overhead\n\nLook UP!")
        print("Email Sent")
