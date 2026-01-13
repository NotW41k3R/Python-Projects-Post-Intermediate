from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

LIVE_PAGE="https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LIVE_PAGE)

articles_no = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
# articles_no.click()
# print(articles_no.text)

click_text = driver.find_element(By.LINK_TEXT, value='Reference desk')
# click_text.click()
# print(click_text.text)

search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_button.click()

search_bar = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search_bar.send_keys("Death Adder", Keys.ENTER)