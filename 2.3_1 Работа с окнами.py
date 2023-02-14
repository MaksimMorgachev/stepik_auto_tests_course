from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import pyperclip


# Задание: принимаем alert
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


# Математическая функция для решения задачи на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)
    answer = browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()

    # Блок копирования в буфер обмена ответа на правильно решенное задание
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    print(alert_text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
