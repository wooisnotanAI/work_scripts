#! python3

"""
Your task is to:

Navigate to the login page
Locate the username and password input fields
Fill in your credentials
Click the login button
Verify that you have successfully logged in by checking for an element visible only to logged-in users
"""
#load modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# launch 
driver = webdriver.Chrom()

# navigate to the login page / open driver
driver.get("https://account.proton.me/login?product=mail&language=en")

# wait for the code to load

# fill in credentials

# click the login button

# verify that you have sccuessfully logged in by checking for an element visible only to logged-in users



