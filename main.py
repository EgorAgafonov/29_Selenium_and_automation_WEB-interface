from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://petfriends.skillfactory.ru/new_user')
request_ID_value = driver.find_element(By.ID, 'name')
actions = ActionChains(driver)
actions.click(on_element=None)

