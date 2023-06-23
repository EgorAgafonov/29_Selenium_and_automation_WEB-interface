from selenium import webdriver
from selenium.webdriver.common import by
import time

driver = webdriver.Chrome()
driver.get("https://petfriends.skillfactory.ru")
title = driver.title





# def test_search_example(selenium):
#     """ Search some phrase in google and make a screenshot of the page. """
#
#     # Open google search page:
#     selenium.get('https://google.com')
#
#     time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Find the field for search text input:
#     search_input = selenium.