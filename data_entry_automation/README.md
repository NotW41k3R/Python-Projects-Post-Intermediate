# Data Entry Automation (BeautifulSoup + Selenium)
Completed on Day 53 of 100 Days of Python

A Python automation project that scrapes rental listing data from a Zillow-style website and automatically submits the extracted information into a Google Form.
The script first sends an HTTP request to a Zillow clone site and parses the returned HTML using BeautifulSoup. For each property listing, it extracts the address, monthly rent, and listing link by targeting HTML attributes. The raw text is cleaned, keeping only the essential data needed for form submission.

Once the data is collected, Selenium is used to automate browser interaction with a Google Form. The script opens the form in Chrome and, for each listing, waits explicitly until the input fields are interactable before filling in the address, rent, and link. After submitting the form, it automatically navigates back to submit another response, repeating the process until all listings have been entered.

Skills learned: web scraping with BeautifulSoup, working with HTML attributes, data cleaning and normalization, Selenium browser automation, explicit waits with Expected Conditions, handling dynamic web pages, and building end-to-end automation workflows