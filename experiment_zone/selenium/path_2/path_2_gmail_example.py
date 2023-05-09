from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your actual Gmail email and password
email = "woosician@gmail.com"
password = "your_password"

# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to Gmail's login page
driver.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/")

# Locate the email input field by its type attribute and enter the email
email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)

# Wait for the password input field to load
time.sleep(2)

# Locate the password input field by its type attribute and enter the password
password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for 5 seconds
time.sleep(5)

# Close the browser
driver.quit()
