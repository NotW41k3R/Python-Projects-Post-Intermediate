from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

FORM_LINK="https://forms.gle/cyu8ScHbnr8Hg7uW6"
SITE_LINK="https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=SITE_LINK)

soup = BeautifulSoup(response.text, 'html.parser')
listings = soup.find_all(class_="StyledPropertyCardDataWrapper")
addresses = []
rents = []
links = []
for listing in listings:
    address = listing.find(attrs={"data-test":"property-card-addr"}).get_text(strip=True).replace('|','').replace('#','').replace("  "," ")
    addresses.append(address)

    rent = listing.find(attrs={"data-test":"property-card-price"}).get_text(strip=True).split('+')[0].split('/')[0]
    rents.append(rent)

    link = listing.find(name='a').get('href')
    links.append(link)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get(FORM_LINK)

for i in range(len(addresses)):
    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    rent_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    address_input.send_keys(addresses[i])
    rent_input.send_keys(rents[i])
    link_input.send_keys(links[i])

    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    submit_btn.click()

    submit_another = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    submit_another.click()