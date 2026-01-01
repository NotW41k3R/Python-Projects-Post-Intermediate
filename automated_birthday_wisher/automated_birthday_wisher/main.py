import random
import pandas as pd
import datetime as dt
import smtplib
import os

my_email = os.getenv("EMAIL")
my_password = os.getenv("EMAIL_PASSWORD")

birthdays = pd.read_csv("birthdays.csv")

today = dt.datetime.now()
today_day = today.day
today_month = today.month
letters = []
for i in range(1,4):
    with open(f"letter_templates/letter_{i}.txt", 'r') as letter:
        current_letter = letter.read()
        letters.append(current_letter)

for index, row in birthdays.iterrows():
    if(row["month"]==today_month and row["day"]==today_day):
        chosen_letter = random.choice(letters)
        birthday_letter = chosen_letter.replace('[NAME]', row["name"])
        
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"], msg=f"Subject: Happy Birthday!! \n\n {birthday_letter}")

# More Efficient Version for look up and letter generation
# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])