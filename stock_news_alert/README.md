# Stock News Alert App (Alpha Vantage + NewsAPI)
Completed on Day 36 of 100 Days of Python

A Python-based stock alert application that monitors daily stock price movements and sends an email notification when a significant price change is detected. The app uses Alpha Vantage’s daily time series API to fetch stock closing prices and compares the most recent trading day with the previous trading day to calculate percentage change. The app accounts for weekends and holidays by stepping backward with datetime.timedelta until a valid trading day is found.

When the price change exceeds a defined threshold, the app fetches relevant news articles using the NewsAPI, constrained to a time window between the penultimate trading day and the current date. The top three news headlines are then included in an automated email alert sent via Gmail’s SMTP server. All sensitive credentials and API keys are managed securely using environment variables.

Skills learned: working with multiple REST APIs (Alpha Vantage and NewsAPI), parsing and navigating nested JSON responses, handling real-world date edge cases with `datetime` and `timedelta`, managing environment variables for secure configuration, and sending automated email notifications using SMTP.
