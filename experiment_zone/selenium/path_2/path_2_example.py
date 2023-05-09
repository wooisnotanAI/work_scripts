from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to a simple login form
driver.get("https://www.example.com/login")

# Locate the username input field by its name attribute and enter a username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("example_username")

# Locate the password input field by its name attribute and enter a password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("example_password")

# Locate the submit button by its type attribute and click it
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

# Wait for 2 seconds
time.sleep(2)

# Close the browser
driver.quit()
