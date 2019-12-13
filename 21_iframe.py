from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.maximize_window()

d.get(r'C:\INST\COURSES\SELENIUM/iframe.html')
sleep(3)

iframe = d.find_elements_by_tag_name('iframe')[0]
d.switch_to.frame(iframe)

d.find_element_by_xpath('/html/body/button').click()

alert = d.switch_to.alert
sleep(3)

## To accept alert
alert.accept()

d.switch_to.default_content()
v = d.find_element_by_xpath('/html/body/p').text
print(' value is :', v)

sleep(3)
d.close()