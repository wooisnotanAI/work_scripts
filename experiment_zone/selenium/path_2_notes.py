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
