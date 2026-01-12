import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

EMAIL=os.getenv("SMTP_EMAIL")
PASSWORD=os.getenv("SMTP_PASSWORD")
STATIC_PAGE="https://appbrewery.github.io/instant_pot/"
LIVE_PAGE="https://www.amazon.in/Razer-BlackShark-V2-Headset-RZ04-03240100-R3M1/dp/B09QFYNJMB/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url=LIVE_PAGE,headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

product_name = soup.find(id="productTitle").get_text(strip=True)

whole_price_text = soup.find(name='span', class_='a-price-whole').get_text(strip=True)
whole_price = int(whole_price_text.split(".")[0].replace(",", ""))

# fraction_price_text = soup.find(name='span', class_='a-price-fraction').get_text(strip=True)
# fraction_price = int(fraction_price_text)/100

item_price = whole_price # + fraction_price
buy_price = 4000

if item_price<buy_price:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject:Amazon Price Alert\n\n{product_name} only for {item_price}".encode("utf-8"))