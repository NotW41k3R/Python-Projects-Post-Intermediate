# ISS Overhead Email Notifier
Completed on Day 33 of 100 Days of Python

A Python automation script that monitors the real-time position of the International Space Station and sends an email alert when the ISS is passing overhead during nighttime at a specified location. The script continuously checks the ISS’s latitude and longitude using a public API, compares it with the user’s coordinates, and verifies whether it is currently after sunset before triggering an email notification.

The program integrates multiple external APIs, and uses SMTP to send alerts securely. Email credentials are handled using environment variables, ensuring sensitive information is not hard-coded.

Skills learned: working with APIs and JSON data using requests, geographic coordinate comparison, handling time and date logic with datetime, SMTP email automation, secure credential management with environment variables, and building condition-based automation scripts.
