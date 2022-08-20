# Берем тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайм новый файл
import unittest

# Создаем в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
class test_class_name(unittest.TestCase):
    def test_class_name1(self):
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
        self.assertEqual
        "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")
    
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
# Код, который заполняет обязательные поля  
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("I@I.ru")
    input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
    input4.send_keys("903")
    input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
    input5.send_keys("Hodgepodge street")

# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

# Создаем в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом      
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
class test_class_name(unittest.TestCase):
    def test_class_name2(self):
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
        self.assertEqual
        "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")
        
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("I@I.ru")
    input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
    input4.send_keys("903")
    input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
    input5.send_keys("Hodgepodge street")
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

# Запустите получившиеся тесты из файла 
# Просмотрите отчёт о запуске и найдите последнюю строчку 
