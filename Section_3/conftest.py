from selenium import webdriver
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
        print("\nstart firefox browser for test..")
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe') # Нет библеотеки!
        browser = webdriver.Firefox(firefox_binary=binary)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)