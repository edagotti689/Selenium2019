'''
1. Contains: By using 'contains' function in XPath, we can extract all the elements which matches a particular text value
2. The contain feature has an ability to find the element with partial text.
    Example :- "//h4/a[contains(text(),'SAP M')]"
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

v = driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").text
print(' \n Text is :', v)

## To find element based partial text
v = driver.find_element_by_xpath("//a[contains(text(),'Gm')]").text
print(' \n Text is :', v)

## To find element based attribute value
v = driver.find_element_by_xpath("//a[contains(@data-pid,'2')]").text
print(' \n Text is :', v)
time.sleep(10)

# Close a browser
driver.close()


