from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element_by_id('input_value').text
def calc(x_element):
  return str(math.log(abs(12*math.sin(int(x_element)))))
y = calc(x_element)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
button.click()

