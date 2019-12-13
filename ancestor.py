'''
ancestor:
    1. The ancestor axis selects all ancestors element (grandparent, parent, etc.) of the current node.

'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(3)

# get text using child axis method xpath
driver.find_element_by_xpath("//input[@name='pass']/ancestor::tr/td[1]/input").send_keys('sriram.python111@gmail.com')
#print(' \n ', text)


time.sleep(10)



# Close a browser
driver.close()



