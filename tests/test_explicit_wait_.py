from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_google():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    try:
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
        'body/div[1]/div[2]/div[1]/img')))
    except:
        print("some error happen !!")
