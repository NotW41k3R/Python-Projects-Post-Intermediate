from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

LIVE_PAGE="https://www.python.org"

driver = webdriver.Chrome(options=chrome_options)
driver.get(LIVE_PAGE)

event_date = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery .menu li time')
event_date_list = [event.text for event in event_date]
print(event_date_list)

event_name_obj = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery .menu li a')
event_name_list = [event.text for event in event_name_obj]
print(event_name_list)

event_dict = {
    i: {"date": t, "event": e}
    for i, (t, e) in enumerate(zip(event_date_list, event_name_list))
}

print(event_dict)