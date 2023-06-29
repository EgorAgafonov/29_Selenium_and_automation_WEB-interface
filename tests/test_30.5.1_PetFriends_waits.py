from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import pytest
import pytest_selenium
import time

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

def test_show_my_pets():
    pytest.driver.find_element(By.ID, "email").send_keys('fonovagafonov@yandex.ru')
    time.sleep(2)

    pytest.driver.find_element(By.ID, "pass").send_keys('123456')
    time.sleep(2)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    try:
        images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
        descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    except:
        print('Неверно указаны CSS-локаторы элементов!')

