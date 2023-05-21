Sure, here are some commonly used properties and methods in the Selenium WebDriver (`driver`) instance along with their Python object types:

1. `driver.title` (str): Returns the title of the current page.

2. `driver.current_url` (str): Returns the URL of the current page.

3. `driver.page_source` (str): Returns the source code of the current page.

4. `driver.window_handles` (list): Returns the handles of all windows opened by the driver.

5. `driver.current_window_handle` (str): Returns the handle of the current window.

6. `driver.name` (str): Returns the name of the underlying driver, e.g., 'chrome', 'firefox' etc.

And here are some commonly used methods:

1. `driver.get("url")` (None): Loads a web page in the current browser session.

2. `driver.find_element_by_*` (WebElement): These are methods used to locate elements on the page, where the * could be `id`, `name`, `class_name`, `css_selector`, `link_text`, `partial_link_text`, `tag_name`, `xpath`.

3. `driver.quit()` (None): Closes all the windows and ends the browser session.

4. `driver.close()` (None): Closes the current window.

5. `driver.back()` (None): Navigates to the previous page.

6. `driver.forward()` (None): Navigates to the next page.

7. `driver.refresh()` (None): Refreshes the current page.

8. `driver.switch_to.alert` (Alert): Switches the focus to an alert on the page.

9. `driver.switch_to.window` (None): Switches focus between windows.

10. `driver.execute_script` (varies): Executes JavaScript within the current window/frame. The return type of this method will depend on the return type of the JavaScript being executed.

Remember that these are just some of the common properties and methods available in the WebDriver object. Depending on your needs, there may be other properties and methods that are also useful for your specific situation.


==========
The Selenium WebDriver provides several methods to locate elements using the `By` class. Here are the most common ones:

1. **By.ID**: Finds the element by its ID.
   ```python
   element = driver.find_element(By.ID, "element_id")
   ```

2. **By.NAME**: Finds the element by its name attribute.
   ```python
   element = driver.find_element(By.NAME, "element_name")
   ```

3. **By.CLASS_NAME**: Finds the element by its class.
   ```python
   element = driver.find_element(By.CLASS_NAME, "class_name")
   ```

4. **By.TAG_NAME**: Finds the element by its tag name.
   ```python
   element = driver.find_element(By.TAG_NAME, "tag_name")
   ```

5. **By.LINK_TEXT**: Finds the link by its text.
   ```python
   element = driver.find_element(By.LINK_TEXT, "link_text")
   ```

6. **By.PARTIAL_LINK_TEXT**: Finds the link by partial match of its text.
   ```python
   element = driver.find_element(By.PARTIAL_LINK_TEXT, "partial_link_text")
   ```

7. **By.CSS_SELECTOR**: Finds the element by its CSS selector.
   ```python
   element = driver.find_element(By.CSS_SELECTOR, "tag#id.class")
   ```

Please note that these methods return the first matching element, so if there are multiple elements matching the locator, these methods will return the first one they find. If you want to find all matching elements, use `driver.find_elements()` instead of `driver.find_element()`.