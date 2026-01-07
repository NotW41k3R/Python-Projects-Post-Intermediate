# Flight Deal Tracker (Amadeus Flight Search + Sheety)
Completed on Day 39 of 100 Days of Python

A Python-based flight deal tracking app that monitors flight prices from a fixed origin city to multiple destinations and sends an email alert when a cheaper than expected flight is found. Destination cities and target prices are stored in a Google Sheet, which is accessed and updated using the Sheety API.

The app first retrieves destination data from the sheet and fills in missing IATA airport codes using Amadeus’s city search API. It then searches for round-trip flights within a configurable date range using the Amadeus Flight Offers Search API, parses the returned data to identify the cheapest available flight, and compares it against the stored price threshold. If a lower price is detected, an automated email notification is sent with the flight details.

All API credentials and sensitive information are managed using environment variables. The project demonstrates how to coordinate multiple APIs, handle authentication flows, parse nested JSON responses, manage rate limits with deliberate delays, and trigger notifications based on business logic.

Skills learned: working with OAuth-protected REST APIs, parsing complex nested JSON structures, comparing dynamic API data against stored values, integrating Google Sheets as a lightweight database via Sheety and sending email notifications using SMTP