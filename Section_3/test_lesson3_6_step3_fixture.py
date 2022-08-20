import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура открытия/закрытия браузера
@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
# Дождаться, загрузки поля для ввода ответа (ожидание нужно установить 10 секунд)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

# Объявляем Класс наименование которого начинается с Test
class TestAnswer:
    #correct = ""
# Входной параметр передачи массива url-адресов для открытия страниц
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"])
# Функция наименование который начинается с Test
# В функцию передаются (self, фикстуру browser, links)
    def test_links(self, browser, links):
# Объявляем переменную - link и присваиваем ей значение links
        link = links
        browser.get(link)
# Объявляем переменную - answer
        answer = math.log(int(time.time()))
# Добавляем ожидание, чтобы ввести значение answer в поле текстового ввода
        browser.implicitly_wait(10)
# Найходим в HTML коде селектор для поиска поля текстового ввода
        input1 = browser.find_element(By.CLASS_NAME, "ember-text-area")
# Применяем переменную answer в поле input1 объявляем ей тип - string
        input1.send_keys(str(answer))
# Добавляем ожидание, чтобы найти в HTML коде кнопку button
        browser.implicitly_wait(10)
# Находим через селектор в HTML коде кнопку - Отправить добавива ожидание на кликабельность кнопки (ожидание 10 секунд)
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
# Нажать кнопку "Отправить"
        button.click()
# # Проверяем,что ожидаемый текст переменной answer в опциональном фидбеке полностью совпадает и
# объявляем переменную правильности ответа - correct и добавляем ожидание до появления текста в 10 секунд
        correct = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
# с переменной correct - преобразованной функцией .text
        assert correct.text == 'Correct!', "not correct!"
        print(correct.text)
# Присваиваем служебной переменной name значение mane
        if __name__ == "__main__":
            pytest.main()













