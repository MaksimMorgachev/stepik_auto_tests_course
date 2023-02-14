from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
import pyperclip

# Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.
#
# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.


# Математическая функция для решения задачи на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
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
