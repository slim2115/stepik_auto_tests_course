from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys("Кот")
    driver.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Матроскин")
    driver.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("matros72@mail.ru")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    driver.quit()