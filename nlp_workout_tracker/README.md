# Workout Tracking App (NLP Exercise API + Sheety)
Completed on Day 38 of 100 Days of Python

A Python-based workout logging application that converts natural language exercise descriptions into structured data and stores them automatically in a Google Sheet. The app uses a custom exercise API provided by the course, which leverages a natural language model (NLM) to parse plain English input (e.g., “ran for 30 minutes”) into a structured JSON response containing exercise name, duration, and calories burned.

The parsed exercise data is then sent to the Sheety API, which inserts the information into a predefined Google Sheet along with the current date and time. All API credentials and sensitive information are managed using environment variables, and authenticated requests are made using custom HTTP headers.

Skills learned: working with natural language–powered APIs, making authenticated HTTP requests, parsing structured JSON responses, chaining multiple REST APIs together, handling date and time formatting with `datetime`, and securely managing API keys using environment variables.