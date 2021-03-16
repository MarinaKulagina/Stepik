from  selenium import webdriver
import os

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)
browser.find_element_by_css_selector('input[name="firstname"]').send_keys("Vanya")
browser.find_element_by_css_selector('[name="lastname"]').send_keys('gggg')
browser.find_element_by_css_selector('[name="email"]').send_keys('hhh@hh.ru')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test.txt"
file_path = os.path.join(current_dir, file_name)
browser.find_element_by_id('file').send_keys(file_path)
browser.find_element_by_css_selector('.btn.btn-primary').click()

