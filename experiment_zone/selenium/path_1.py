from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to example.com
driver.get("https://www.example.com")

# Wait for 2 seconds
time.sleep(2)

# Go to another URL
driver.get("https://www.wikipedia.org")

# Wait for 2 seconds
time.sleep(2)

# Go back in browser history
driver.back()

# Wait for 2 seconds
time.sleep(2)

# Go forward in browser history
driver.forward()

# Wait for 2 seconds
time.sleep(2)

# Refresh the current page
driver.refresh()

# Wait for 2 seconds
time.sleep(2)

# Close the browser
driver.quit()
