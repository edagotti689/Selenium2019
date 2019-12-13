'''
Preceding:
    1.Select all nodes that come before the current node
following:
    1.Select all nodes that come after the current node
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(3)

# Enter user name based on password xpath
email = driver.find_element_by_xpath('//input[contains(@id,"pass")]/preceding::input[1]')
email.send_keys('sriram.python11@gamil.com')
time.sleep(5)

# Enter password based on uname xpath
email = driver.find_element_by_xpath('//input[contains(@id,"email")]/following::input[1]')
email.send_keys('sri')

time.sleep(10)

# Close a browser
#driver.close()



