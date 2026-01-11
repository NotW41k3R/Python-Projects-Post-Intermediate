import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
names = soup.find_all(name = 'h3', class_ = 'title')
name_list = [name.get_text(strip=True) for name in names]
name_list.reverse()

for name in name_list:
    print(name)