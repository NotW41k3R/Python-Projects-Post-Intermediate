import requests
import datetime as dt
import smtplib
import os

my_email=os.environ.get("EMAIL")
my_password=os.environ.get("PASSWORD")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY1 = os.environ.get("API_KEY1") #alphavantage api
API_KEY2 = os.environ.get("API_KEY2") #newsapi

url1 = "https://www.alphavantage.co/query"
parameters1 = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : API_KEY1,
}

def get_news(today,penultimate_date):
    url = "https://newsapi.org/v2/everything"
    parameters = {
        'q': 'Tesla OR TSLA OR "Tesla Inc"',
        'apiKey' : API_KEY2,
        'from' : penultimate_date,
        'to' : today,
        'sortBy' : 'popularity',
        'pageSize': 3,
    }
    news = requests.get(url=url,params=parameters)
    news.raise_for_status()
    return news.json()

def date_to_string(date_obj):
    return date_obj.strftime("%Y-%m-%d")

def previous_market_day(date, data):
    date_str = date_to_string(date)
    while date_str not in data:
        date = date - dt.timedelta(days=1)
        date_str = date_to_string(date)
    return date

response1 = requests.get(url=url1,params=parameters1)
response1.raise_for_status()
trading_data = response1.json()['Time Series (Daily)']

today = dt.datetime.today().date()
today_str = date_to_string(today)

last_market_day = previous_market_day(today,trading_data)
penultimate_market_day = previous_market_day(last_market_day - dt.timedelta(days=1),trading_data)

last_market_day_str = date_to_string(last_market_day)
penultimate_market_day_str =date_to_string(penultimate_market_day)

closing_last_day = float(trading_data[last_market_day_str]['4. close'])
closing_penultimate_day = float(trading_data[penultimate_market_day_str]['4. close'])

percent_diff = ((closing_last_day-closing_penultimate_day)/closing_penultimate_day)*100

if abs(percent_diff)>2:
    news = get_news(today_str,penultimate_market_day_str)['articles']
    titles = []
    for article in news:
        title = article['title']
        titles.append(title)

    per_diff = round(percent_diff,2)
    if percent_diff>0:
        subject = f'TSLA: UP {per_diff}%'
    else:
        subject = f'TSLA: DOWN {per_diff}%'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: {subject}\n\n{titles[0]}\n{titles[1]}\n{titles[2]}")
