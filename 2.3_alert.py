from selenium import webdriver
import math


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
browser.find_element_by_tag_name('button').click()
alert = browser.switch_to.alert
alert.accept()
x = browser.find_element_by_id('input_value').text
def chet (x):
    return str(math.log(abs(12 * math.sin(int(x)))))
y = chet(x)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_css_selector('.btn.btn-primary').click()


