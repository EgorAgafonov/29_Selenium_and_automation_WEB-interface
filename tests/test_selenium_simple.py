from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """


    selenium.get("https://google.com")  # - метод get загружает страницу по указанному адресу
    time.sleep(3)  # - метод sleep дает задержку выполнения следующей строки кода (команды) для целей полной загрузки
    # страницы перед отправкой следующей команды

    search_input = selenium.find_element(By.NAME, "q")  # поиск элемента по имени (тэгу) на странице с помощью метода
    # .find_element(By.NAME, "element's name")
    search_input.clear()  # очистка текста, если метод clear применяется к элементу для ввода текста (поле ввода)
    search_input.send_keys("qwerty") # симуляция печати клавишами букв "qwe" методом .send_keys для ввода
    time.sleep(3)
    # текста в поле поиска

    search_button = selenium.find_element(By.NAME, "btnK")
    search_button.click()
    time.sleep(3)

    selenium.save_screenshot('result.png')

