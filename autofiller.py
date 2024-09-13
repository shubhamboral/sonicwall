import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Firefox browser
driver = webdriver.Firefox()

# Open the specified URL
driver.get("https://172.29.0.1:8090/sonicui/7/login/#/?cid=5")

# Wait for the username field to be located
username_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="Enter your username..."]')))
# Wait for the password field to be located
password_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="Enter your password..."]')))

# Open the credentials file and select a random set of credentials
with open("./credentials.txt", "r") as f:
    lines = f.readlines()
    login = random.randint(0, len(lines) - 1)
    credentials = lines[login].strip().split(",")

# Type the username character by character
for char in credentials[0]:
    username_field.send_keys(char)

# Type the password character by character
for char in credentials[1]:
    password_field.send_keys(char)

# Press the Enter key after entering the password
password_field.send_keys(Keys.RETURN)

# Wait for the URL to change to the confirmation page
WebDriverWait(driver, 15).until(EC.url_matches("https://172.29.0.1:8090/sonicui/7/login/#/confirm"))

# After the URL matches, press Enter
if "confirm" in driver.current_url:
    # Press Enter to proceed
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.RETURN)
    print("Login successful with username", credentials[0], "and password", credentials[1])
else:
    print("Login failed.")
