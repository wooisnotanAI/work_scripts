# pylint: disable=unspecified-encoding
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

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

# Find the username and password input elements
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

# Enter the credentials
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Close the browser
driver.quit()
