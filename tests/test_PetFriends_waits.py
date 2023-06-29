from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import pytest_selenium
import time


driver = webdriver.Chrome('путь до драйвера/chromedriver.exe')
driver.get('http://petfriends.skillfactory.ru/login')


                                                 # Неявные ожидания

def test_implicitly_wait_my_pets():
    """Блок тестов implicitly_wait (неявные ожидания) на основе библиотеки Selenium для проверки загрузки элементов
    карточки питомца на платформе http://petfriends.skillfactory.ru."""

    driver.find_element(By.ID, "email").send_keys('указать зарегистрированный email')
    time.sleep(2)
    driver.find_element(By.ID, "pass").send_keys('указать зарегистрированный password')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    # 1. Проверка неявного ожидания элемента - фото питомца по CSS-локатору. Проверка инструкцией assert по наличию
    # атрибута class с верным значением.
    driver.implicitly_wait(2)
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    pet_photo = driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(2) > div > div')
    assert pet_photo.get_attribute('class') == 'text-center align-self-center align-middle'

    # 2. Проверка неявного ожидания элемента - имя питомца по CSS-локатору. Проверка инструкцией assert на наличие
    # в найденном элементе имени питомца (любого строкового значения).
    driver.implicitly_wait(2)
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    pet_name = driver.find_element(By.CSS_SELECTOR, '.card-deck .card-title')
    assert pet_name.text != ''

    # 3. Проверка неявного ожидания элемента - возраста питомца по CSS-локатору. Проверка инструкцией assert на наличие
    # в найденном элементе возраста питомца (любого строкового значения).
    driver.implicitly_wait(2)
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    pet_age = driver.find_element(By.CSS_SELECTOR, '.card-deck .card-text')
    assert pet_age.text != ''

                                                # Явные ожидания

def test_explicit_wait_my_pets():
    """Блок тестов explicit_wait (явные ожидания) на предмет загрузки множества элементов страницы
    (проверка таблицы питомцев) на платформе http://petfriends.skillfactory.ru."""

    driver.find_element(By.ID, "email").send_keys('указать зарегистрированный email')
    time.sleep(2)
    driver.find_element(By.ID, "pass").send_keys('указать зарегистрированный password')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    # 1. ВНИМАНИЕ! Тест валиден только в случае, если все карточки питомцев на сайте имеют загруженное фото!
    # С помощью класса WebDriverWait и метода presence_of_all_elements_located () выполним процедуру явного ожидания
    # загрузки на странице множества элементов с фото питомцев и определим переменную для их хранения. После чего с
    # помощью цикла for in range и инструкции assert проверим полученные элементы на предмет наличия в них обязательного
    # атрибута 'src'.
    pets_photos = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
    '.card-deck .card-img-top')))
    for photo in range(len(pets_photos)):
        assert pets_photos[photo].get_attribute('src') != ''


    # 2. ВНИМАНИЕ ! Тест валиден только в случае, если у всего списка питомцев на сайте в карточках указано имя!
    # С помощью класса WebDriverWait и метода presence_of_all_elements_located () выполним процедуру явного ожидания
    # загрузки на странице множества элементов с именами питомцев и определим переменную для их хранения. После чего с
    # помощью цикла for in range и инструкции assert проверим полученные элементы на предмет наличия в них атрибутов с
    # текстом (поля с именами питомцев не пустые).
    pets_names = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
    '.card-deck .card-title')))
    for name in range(len(pets_names)):
        assert pets_names[name].text != ''


    # 3. ВНИМАНИЕ ! Тест валиден только в случае, если у всего списка питомцев на сайте в карточках указан возраст!
    # С помощью класса WebDriverWait и метода presence_of_all_elements_located () выполним процедуру явного ожидания
    # загрузки на странице множества элементов с указанным возрастом питомцев и определим переменную для их хранения.
    # После чего с помощью цикла for in range и инструкции assert проверим полученные элементы на предмет наличия в
    # них атрибутов с указанным возрастом питомца (поля с возрастом питомцев не пустые).
    pets_age = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
    '.card-deck .card-text')))
    for age in range(len(pets_age)):
        assert pets_age[age].text != ''
