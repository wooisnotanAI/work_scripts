# This is not a functional / runnable code, this is a notebook.

from selenium.webdriver.common.by import By

# Locate an element by ID
element_by_id = driver.find_element(By.ID, "element_id")

# Locate an element by name
element_by_name = driver.find_element(By.NAME, "element_name")

# Locate an element by class name
element_by_class_name = driver.find_element(
    By.CLASS_NAME, "element_class_name")

# Locate an element by CSS selector
element_by_css_selector = driver.find_element(By.CSS_SELECTOR, "css_selector")

# Locate an element by link text
element_by_link_text = driver.find_element(By.LINK_TEXT, "link_text")

# Locate an element by partial link text
element_by_partial_link_text = driver.find_element(
    By.PARTIAL_LINK_TEXT, "partial_link_text")


# Send text to an input field
element.send_keys("example text")

# Click on a button or link
element.click()

# Clear the text of an input field
element.clear()

# Get an attribute value of an element
attribute_value = element.get_attribute("attribute_name")

# Get the text content of an element
element_text = element.text


# So then the basics are locating elements, then interacting with them.
############# new section ####

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# 1. By.ID
element_by_id = driver.find_element(By.ID, "element_id")

# 2. By.NAME
element_by_name = driver.find_element(By.NAME, "element_name")

# 3. By.CLASS_NAME
element_by_class = driver.find_element(By.CLASS_NAME, "element_class")

# 4. By.TAG_NAME
element_by_tag = driver.find_element(By.TAG_NAME, "tag_name")

# 5. By.XPATH
element_by_xpath = driver.find_element(By.XPATH, "//tag_name[@attribute='value']")

# 6. By.CSS_SELECTOR
element_by_css = driver.find_element(By.CSS_SELECTOR, "tag_name.attribute[value='value']")

# 7. By.LINK_TEXT
element_by_link_text = driver.find_element(By.LINK_TEXT, "Link Text")

# 8. By.PARTIAL_LINK_TEXT
element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Link Text")
