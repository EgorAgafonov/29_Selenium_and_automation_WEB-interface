from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
# from conftest import driver_args
import time


# def test_petfriends(selenium):
#     # Open PetFriends base page:
#     selenium.get("https://petfriends.skillfactory.ru/")
#
#     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # click on the new user button
#     btn_new_user = selenium.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
#     btn_new_user.click()
#     time.sleep(2)
#
#     # click existing user button
#     btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
#     btn_exist_acc.click()
#     time.sleep(2)
#
#     # add email
#     field_email = selenium.find_element(By.ID, "email")
#     field_email.clear()
#     field_email.send_keys("fonovagafonov@yandex.ru")
#     time.sleep(2)
#
#     # add password
#     field_pass = selenium.find_element (By.ID, "pass")
#     field_pass.clear()
#     field_pass.send_keys("123456")
#     time.sleep(2)
#
#     # click submit button
#     btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
#     btn_submit.click()
#     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
#
#     if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
#         # Make the screenshot of browser window:
#         selenium.save_screenshot('result_petfriends.png')
#     else:
#         raise Exception("Login error")

def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_new_user = web_browser.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
    btn_new_user.click()
    time.sleep(2)

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()
    time.sleep(2)

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("fonovagafonov@yandex.ru")
    time.sleep(2)

    # add password
    field_pass = web_browser.find_element (By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("123456")
    time.sleep(2)

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()
    time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!

    assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"