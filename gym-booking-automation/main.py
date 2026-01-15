import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

EMAIL = "admin@test.com"
PASSWORD="THISISAPASSWORD"
URL="https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 2)

driver.get(URL)

def login():
    driver.find_element(By.ID, "login-button").click()

    wait.until(ec.presence_of_element_located((By.ID, "test-credentials")))

    driver.find_element(By.ID, "email-input").send_keys(EMAIL)
    print("filled")
    driver.find_element(By.ID, "password-input").send_keys(PASSWORD)
    print("filled")
    attempt = 0
    while True:
        attempt += 1
        driver.find_element(By.ID, "submit-button").click()
        print("pressed")
        time.sleep(3)

        errors = driver.find_elements(By.ID, "error-message")
        
        if not errors:
            print(f"Login succeeded after {attempt} attempts")
            break
        else:
            print(f"Login failed (attempt {attempt}), retrying...")
login()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_cnt = 0
waitlist_cnt = 0
already_booked_cnt = 0
total_bookings = booked_cnt + waitlist_cnt + already_booked_cnt

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    gym_days = ["Tue", "Thu"]
    for day in gym_days:
        if day in day_title:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            if button.text == "Booked":
                print(f"Already booked: {class_name} on {day_title}")
                already_booked_cnt += 1
            elif button.text == "Waitlisted":
                print(f"Already on waitlist: {class_name} on {day_title}")
                already_booked_cnt += 1
            elif button.text == "Book Class":
                button.click()
                print(f"Successfully booked: {class_name} on {day_title}")
                booked_cnt += 1
                time.sleep(0.3)
            elif button.text == "Join Waitlist":
                button.click()
                print(f"Joined waitlist for: {class_name} on {day_title}")
                waitlist_cnt += 1
                time.sleep(0.3)

print("\nSummary")
print(f"Classes booked: {booked_cnt}")
print(f"Waitlists joined: {waitlist_cnt}")
print(f"Already booked/waitlisted: {already_booked_cnt}")
print(f"Total classes processed: {total_bookings}")

my_booking_btm = driver.find_element(By.ID, value="my-bookings-link")
my_booking_btm.click()

cnf_bookings = driver.find_elements(By.CSS_SELECTOR, value='.MyBookings_bookingCard__VRdrR')
waiting = driver.find_elements(By.CSS_SELECTOR, value='.MyBookings_bookingCard__VRdrR MyBookings_waitlist__rD_tl')

verified_bookings = len(cnf_bookings) + len(waiting)
print(f"Verified Bookings: {verified_bookings}")