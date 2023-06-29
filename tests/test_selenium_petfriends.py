# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common import keys
# import pytest
# import pytest_selenium
# import time
#
#
# # def test_petfriends(selenium):
# #     # Open PetFriends base page:
# #     selenium.get("https://petfriends.skillfactory.ru/")
# #
# #     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
# #
# #     # click on the new user button
# #     btn_new_user = selenium.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
# #     btn_new_user.click()
# #     time.sleep(2)
# #
# #     # click existing user button
# #     btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
# #     btn_exist_acc.click()
# #     time.sleep(2)
# #
# #     # add email
# #     field_email = selenium.find_element(By.ID, "email")
# #     field_email.clear()
# #     field_email.send_keys("fonovagafonov@yandex.ru")
# #     time.sleep(2)
# #
# #     # add password
# #     field_pass = selenium.find_element (By.ID, "pass")
# #     field_pass.clear()
# #     field_pass.send_keys("123456")
# #     time.sleep(2)
# #
# #     # click submit button
# #     btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
# #     btn_submit.click()
# #     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
# #
# #     if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
# #         # Make the screenshot of browser window:
# #         selenium.save_screenshot('result_petfriends.png')
# #     else:
# #         raise Exception("Login error")
#
# # def test_petfriends(web_browser):
# #     # Open PetFriends base page:
# #     web_browser.get("https://petfriends.skillfactory.ru/")
# #
# #     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
# #
# #     # click on the new user button
# #     btn_new_user = web_browser.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
# #     btn_new_user.click()
# #     time.sleep(2)
# #
# #     # click existing user button
# #     btn_exist_acc = web_browser.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
# #     btn_exist_acc.click()
# #     time.sleep(2)
# #
# #     # add email
# #     field_email = web_browser.find_element(By.ID, "email")
# #     field_email.clear()
# #     field_email.send_keys("fonovagafonov@yandex.ru")
# #     time.sleep(2)
# #
# #     # add password
# #     field_pass = web_browser.find_element(By.ID, "pass")
# #     field_pass.clear()
# #     field_pass.send_keys("123456")
# #     time.sleep(2)
# #
# #     # click submit button
# #     btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
# #     btn_submit.click()
# #     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
# #
# #     assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
#
#
# @pytest.fixture(autouse=True)
# def testing():
#     pytest.driver = webdriver.Chrome('tests/chromedriver.exe')
#     pytest.driver.get('http://petfriends.skillfactory.ru/login')
#     yield
#     pytest.driver.quit()
#
#
# def test_show_my_pets():
#     pytest.driver.find_element(By.ID, "email").send_keys('fonovagafonov@yandex.ru')
#     time.sleep(2)
#
#     pytest.driver.find_element(By.ID, "pass").send_keys('123456')
#     time.sleep(2)
#
#     pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     assert pytest.driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"
#
#     images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
#     names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
#     descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
#
#     for i in range(len(names)):
#         assert images[i].get_attribute('src') != ''
#         assert names[i].text != ''
#         assert descriptions[i].text != ''
#         assert ', ' in descriptions[i]
#         parts = descriptions[i].text.split(', ')
#         assert len(parts[0]) > 0
#         assert len(parts[1]) > 0
