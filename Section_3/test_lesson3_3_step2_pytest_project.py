# Берем тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайм новый файл

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import unittest
import time


def get_text(link):
    # функция заполнения формы регистрации возвращает строку заголовка страницы после регистрации
    # browser закроется после выполнения скрипта сам
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    browser.find_element("xpath", '//input[@placeholder="Input your first name"]').send_keys("Ivan")
    browser.find_element("xpath", '//input[@placeholder="Input your last name"]').send_keys("Petrov")
    browser.find_element("xpath", '//input[@placeholder="Input your email"]').send_keys("I@I.ru")
    browser.find_element("xpath", '//input[@placeholder="Input your phone:"]').send_keys("903")
    browser.find_element("xpath", '//input[@placeholder="Input your address:"]').send_keys("Hodgepodge street")

    # Отправляем заполненную форму
    button = browser.find_element("xpath", "//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # ожидаем появление элемента "заголовок страницы", содержащего текст
    welcome_text_elt = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    # записываем полученный текст в переменную
    welcome_text = welcome_text_elt.text
    return welcome_text

# класс для тестов
class TestLink(unittest.TestCase):

    def test_link1(self):
    # ссылки заданий

        self.assertEqual(get_text("http://suninjuly.github.io/registration1.html"),
    # Ожидаемое значение в заголовке страницы после регистрации
                         "Congratulations! You have successfully registered!",
                         "Registration failed")

    def test_link2(self):
    # ссылки заданий
        self.assertEqual(get_text("http://suninjuly.github.io/registration2.html"),
    # Ожидаемое значение в заголовке страницы после регистрации
                         "Congratulations! You have successfully registered!",
                         "Registration failed")


if __name__ == "__main__":
    unittest.main()
