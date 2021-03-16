
from selenium import webdriver
import math
import time

# link = "http://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# x = browser.find_element_by_id('treasure').get_attribute("valuex")
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# y = calc(x)
# browser.find_element_by_id("answer").send_keys(y)
# browser.find_element_by_id("robotCheckbox").click()
# browser.find_element_by_id("robotsRule").click()
# browser.find_element_by_css_selector('.btn.btn-default').click()

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"


