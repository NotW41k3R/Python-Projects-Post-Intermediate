# Amazon Price Tracker
Completed on Day 47 of 100 Days of Python

A Python script that tracks the live price of an Amazon product and sends an email alert when the price drops below a predefined target.

The script fetches the product page using custom HTTP headers to mimic a real browser, parses the HTML with BeautifulSoup, and extracts the product name and current price. The price is cleaned and converted into an integer for comparison against a user-defined buy price. When the price falls below the threshold, an automated email notification is sent using SMTP server. All sensitive credentials are managed securely using environment variables.

Skills learned: web scraping with BeautifulSoup, handling HTTP headers, cleaning scraped data, managing environment variables, and sending emails via SMTP