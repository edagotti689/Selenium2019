'''
Start-with function finds the element whose attribute value

changes on refresh or any operation on the webpage.In this expression, match the starting text of the attribute is used to find the element whose attribute changes dynamically. You can also find the element whose attribute value is static (not changes).

For example -: Suppose the ID of particular element changes dynamically like:
    Id=" message12"
    Id=" message345"
    Id=" message8769"
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

v = driver.find_element_by_xpath("//a[starts-with(text(),'Gm')]").text

print(' \n Text is :', v)
time.sleep(10)

# Close a browser
#driver.close()



