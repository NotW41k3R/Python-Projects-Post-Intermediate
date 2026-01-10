import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all(name = 'span', class_ = 'titleline')
article_titles = []
article_links = []

for article_tag in articles:
    title = article_tag.a.getText()
    link = article_tag.a.get('href')
    article_titles.append(title)
    article_links.append(link)
article_scores = [int(score.getText().split(" ")[0]) for score in soup.find_all(name = 'span', class_='score')]

max_index = article_scores.index(max(article_scores))
print(article_scores[max_index])
print(article_titles[max_index])
print(article_links[max_index])
