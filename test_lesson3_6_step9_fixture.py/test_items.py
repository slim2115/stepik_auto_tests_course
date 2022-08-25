import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', 'browser', ["ru", "en-gb"])
def test_guest_should_see_button_add_in_basket_on_the_product_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/"
    time.sleep(30)
    browser.get(link)
# Находим через селектор в HTML коде кнопку - Добавить в карзину
    basket = browser.find_element(By.CLASS_NAME, "btn btn-lg btn-primary btn-add-to-basket")
# В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы
    assert basket.text, "button_add_basket_not_found!"
    print(basket.text)
# Присваиваем служебной переменной name значение mane
    if __name__ == "__main__":
        pytest.main()



