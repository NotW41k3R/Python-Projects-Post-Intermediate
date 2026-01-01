import smtplib
import datetime as dt
import random
import os

with open("quotes.txt") as file:
    quotes = file.readlines()

my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")

current_quote = random.choice(quotes)

current_time = dt.datetime.now()

if not current_time.weekday():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email , password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Quote\n\n{current_quote}")
    