#! python3

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



# Read the credentials from "pw.txt"
# If you don't already, you must create a pw.txt in the same directory as this script for it to run.
filename = "pw.txt"
current_path = os.path.dirname(__file__)
filepath = os.path.join(current_path, filename)

with open(f"{filepath}", "r") as file:
    username = file.readline().strip()
    password = file.readline().strip()

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://production-admin.tallyup.com/ui/")

# Define a wait time (e.g., 10 seconds)
wait = WebDriverWait(driver, 10)

# Wait for the element to be present and visible, then find it
username_input = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "input[placeholder='Username']")))


# Find the username and password input elements
username_input = driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Username']")
password_input = driver.find_element(
    By.CSS_SELECTOR, "input[placeholder='Password']")


# Enter the credentials
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.RETURN)

#press the login button;
button = driver.find_element(By.CSS_SELECTOR, "div.button")
button.click()

#wait for login
wait = WebDriverWait(driver, 10)

#wait to redirect
wait = WebDriverWait(driver, 30)
time.sleep(5)

driver.get("https://production-admin.tallyup.com/ui/cashouts/list")
time.sleep(15)


# Find the dropdown menu element
dropdown = driver.find_element(By.CLASS_NAME, "el-select__caret")

# Click the dropdown to open the menu
dropdown.click()

# Wait for the menu options to load (replace "5" with the appropriate time in seconds)
driver.implicitly_wait(5)

# Select an option from the menu (replace "Option 1" with the appropriate option text)
select = Select(driver.find_element(By.CLASS_NAME, "el-select-dropdown__item"))
select.select_by_visible_text("Option 1")


# stop the script for 3 mins
time.sleep(100)
