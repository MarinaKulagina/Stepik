from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    chekbok = browser.find_element_by_id('robotCheckbox')
    chekbok.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    sub = browser.find_element_by_css_selector('.btn.btn-default')
    sub.click()







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

777