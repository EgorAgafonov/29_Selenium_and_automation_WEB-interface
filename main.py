from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://petfriends.skillfactory.ru/new_user')
ID_name = driver.find_element(By.ID, 'name')
actions = ActionChains(driver)
actions.click(on_element=None)

