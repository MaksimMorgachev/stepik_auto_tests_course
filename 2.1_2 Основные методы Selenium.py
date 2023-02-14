from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import pyperclip

# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

# Математическая функция для решения задачи на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    result_calc = calc(x)
    answer = browser.find_element(By.ID, 'answer').send_keys(result_calc)
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule').click()
    btn = browser.find_element(By.CLASS_NAME, 'btn-default').click()

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
