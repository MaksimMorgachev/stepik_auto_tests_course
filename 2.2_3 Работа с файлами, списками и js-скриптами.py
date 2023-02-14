from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import pyperclip
import os
from mimesis import Person
from mimesis.locales import Locale
person = Person(Locale.EN)

# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.


# Математическая функция для решения задачи на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname').send_keys(person.first_name())
    last_name = browser.find_element(By.NAME, 'lastname').send_keys(person.last_name())
    email = browser.find_element(By.NAME, 'email').send_keys(person.email())
    test_file = os.path.abspath('test.txt')
    file = browser.find_element(By.ID, 'file').send_keys(test_file)
    btn = browser.find_element(By.CLASS_NAME, 'btn-primary').click()

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
