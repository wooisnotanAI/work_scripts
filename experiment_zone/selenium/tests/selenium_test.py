import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Read the email and password from the credentials.txt file
filename = "tst_pw.txt"
current_path = os.path.dirname(__file__)
filepath = os.path.join(current_path, filename)


with open(f"{filepath}", "r") as f:
    email, password = f.read().strip().split("\n")

# Set up the webdriver (make sure to replace the path with the actual path to your chromedriver)
driver_path = "/path/to/chromedriver"
browser = webdriver.Chrome(driver_path)

# Open the Gmail login page
browser.get("https://production-admin.tallyup.com/ui/")

# Find email input element and enter the email
email_input = browser.find_element(
    By.CSS_SELECTOR, "input.input[placeholder='Username']")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)

# Wait for the password input to load
time.sleep(2)

# Find password input element and enter the password
password_input = browser.find_element(
    By.CSS_SELECTOR, "input[type='password']")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)


while True:
    time.sleep(100)
