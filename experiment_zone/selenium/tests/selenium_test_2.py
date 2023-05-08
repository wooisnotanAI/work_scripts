from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://example.com"  # Replace with the URL of the website you want to inspect

# Initialize the WebDriver (use the appropriate driver for your browser)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get('https://production-admin.tallyup.com/ui/')

# Find and print images
images = driver.find_elements(By.TAG_NAME, "img")
for image in images:
    print(f"Image: {image.get_attribute('src')}")


inputs = driver.find_elements(By.CLASS_NAME, "input")
for input_elem in inputs:
    print(f"Input element: {input_elem.get_attribute('name')}")

# Close the browser
driver.quit()
