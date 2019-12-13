'''
With text function, we can find the element with exact text match
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

## To find element based partial text
v = driver.find_element_by_xpath("//a[text()='Gmail']").text
print(' \n Text is :', v)

time.sleep(10)

# Close a browser
driver.close()


