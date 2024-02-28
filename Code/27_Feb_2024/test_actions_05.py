import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_actions_05():
    driver = webdriver.Edge()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(5)
    fromCity = driver.find_element(By.ID, 'fromCity')
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()

    time.sleep(20)
