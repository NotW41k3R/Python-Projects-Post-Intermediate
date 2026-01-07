import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.my_email=os.getenv("MY_EMAIL")
        self.my_password=os.getenv("MY_PASSWORD")

    def send_email(self, message_body):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.my_password)
            connection.sendmail(from_addr=self.my_email,to_addrs=self.my_email,msg=message_body.encode("utf-8"))
        print("Email Sent")