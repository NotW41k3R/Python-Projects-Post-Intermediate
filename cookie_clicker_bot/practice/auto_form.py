from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

LIVE_PAGE="https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LIVE_PAGE)

fname = driver.find_element(By.CLASS_NAME, value="top")
fname.send_keys("QWERTY")

lname = driver.find_element(By.CLASS_NAME, value="middle")
lname.send_keys("QWERTY")

email = driver.find_element(By.CLASS_NAME, value="bottom")
email.send_keys("qwerty@qwerty.qwerty")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()