'''
child:
    1. Selects all children elements of the current node.
parent:
    1. Selects the parent of the current node.
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get(r'C:\INST\COURSES\SELENIUM\DYNAMIC_XPATH/child.html')
driver.maximize_window()
time.sleep(3)

# get text using child axis method xpath
text = driver.find_element_by_xpath("//ol[@id='course']/child::li[1]").text
print(' \n ', text)
time.sleep(3)

# get text using parent axis method xpath
text = driver.find_element_by_xpath("//li[4]/parent::ol").text
print(' \n ', text)

time.sleep(10)



# Close a browser
driver.close()



