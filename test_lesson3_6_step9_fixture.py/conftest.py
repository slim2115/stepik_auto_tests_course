from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)

# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
# parser - атрибут объекта request.
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
# request - объект для анализа контекста запрашивающей тестовой функции, класса или модуля.
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    # browser = None
    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart browser firefox for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': '"ru", "en-gb"'})
    browser = webdriver.Chrome(options=options)