'''
1. OR ==>  condition 1 OR condition 2 any one should be true. 
2. AND ==> condition 1 and condition 2 should be true. 

'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

v = driver.find_element_by_xpath("//a[contains(@data-pid,'23') and @class='gb_d']").text

v = driver.find_element_by_xpath("//a[contains(@data-pid,'23') or @class='gb_d']").text


print(' \n Text is :', v)
time.sleep(10)

# Close a browser
driver.close()



