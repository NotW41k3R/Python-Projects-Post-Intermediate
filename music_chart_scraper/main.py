import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100"

date = input("Enter a date in given format(YYYY-MM-DD): ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=f"{BASE_URL}/{date}", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

# with open("billboard.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())


# print(soup.prettify())