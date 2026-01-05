# Rain Alert App (OpenWeather API)
Completed on Day 35 of 100 Days of Python

A Python-based rain alert application that checks the upcoming weather forecast using the OpenWeather 5-day / 3-hour forecast API and sends an email notification if rain is expected in the near future.

The app fetches forecast data for a given latitude and longitude, extracts weather condition codes, and determines whether rain-related conditions are present. If rain is detected, the program sends an automated email alert using Gmail’s SMTP server. All sensitive credentials (email, password, API key) are securely managed using environment variables.

Skills learned: working with REST APIs and query parameters, parsing nested JSON data, using environment variables for secure credential management, sending emails via SMTP.
