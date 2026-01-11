# Web Scraping (Movies & Hacker News)

Completed on Day 45 of 100 Days of Python

A small Python project focused on learning web scraping, specifically understanding HTML structure, tags, and CSS-based selection using requests and BeautifulSoup.

The project includes two examples. The first scrapes a static Empire Online movie rankings page (via the Wayback Machine) by extracting movie titles from repeated elements and reordering them to match the original ranking.

The second example scrapes the Hacker News front page to collect article titles, links, and scores. It then compares the scores to find and print the highest-scoring article. This was used to practice navigating nested HTML and extracting text and links from real webpages.

Skills learned: reading and reasoning about HTML trees, using .select(), .find() and .find_all() effectively, extracting text and attributes, applying basic CSS selector logic for scraping, and handling both static and live webpages