from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2) # Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов из-за асинхронной работы скриптов или задержек от сервера, поэтому мы будем ждать появление элемента на странице в течение заданного количества времени (например, 5 секунд). Проверять наличие элемента будем каждые 500 мс. Как только элемент будет найден, мы сразу перейдем к следующему шагу в тесте. Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.
browser.get("http://suninjuly.github.io/cats.html")


button = browser.find_element_by_id('verify')
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text