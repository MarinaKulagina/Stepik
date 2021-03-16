from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)
a = browser.find_element_by_id('num1').text       # Поиск значения элемента
b = browser.find_element_by_id('num2').text
num1 = int(a)
num2 = int(b)
num3 = num1 + num2
select = Select(browser.find_element_by_tag_name('select'))
select.select_by_visible_text(str(num3))
browser.find_element_by_css_selector('.btn.btn-default').click()

