from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # указывая директорию,где лежит файлу.txt
    # в конце должен быть /
    current_dir = os.path.abspath(os.path.dirname("__file.txt__"))
    # имя файла, который будем загружать на сайт
    file_name = "file.txt"
    # получаем путь к file.txt
    file_path = os.path.join(current_dir, "file.txt")
    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
    
finally:
    
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
