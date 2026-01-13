from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

LIVE_PAGE="https://ozh.github.io/cookieclicker/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LIVE_PAGE)

time.sleep(2)

lang_select = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
lang_select.click()

time.sleep(1)
cookie = driver.find_element(By.ID, value="bigCookie")
products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")

last_check = time.time()
interval = 2
time_elapsed = time.time()
while True: 
    time.sleep(0.01)
    if time.time() - time_elapsed >= 60*5:
        break

    cookie.click()

    if time.time() - last_check >= interval:
        products = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
        if products:
            products[-1].click()
            last_check = time.time()

final_cps = driver.find_element(By.XPATH, value='//*[@id="cookiesPerSecond"]')
print(final_cps.text)