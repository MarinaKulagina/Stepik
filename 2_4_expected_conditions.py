# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.implicitly_wait(2)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element_by_id("book")
button.click()
x = browser.find_element_by_id('input_value')
browser.execute_script("return arguments[0].scrollIntoView(true);", x)
rrr = x.text
def chet (rrr):
    return str(math.log(abs(12 * math.sin(int(rrr)))))
y = chet(rrr)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()
m


