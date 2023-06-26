from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    selenium.get("https://google.com")

    time.sleep(3)

    search_input = selenium.find_element(By.NAME, "q")
    search_input.clear()
    search_input.send_keys("qwe")

    time.sleep(3)

    search_button = selenium.find_element(By.NAME, "btnK")
    search_button.submit()

    time.sleep(10)

    selenium.save_screenshot('result.png')

