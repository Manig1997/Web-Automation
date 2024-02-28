import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

def test_actions_02():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #clickable = driver.find_element(By.ID, "clickable")
    #actions = ActionChains(driver)
    #actions.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("mani g").key_up(Keys.SHIFT).perform()
    driver.find_element(By.ID, "click").click()
    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()
    time.sleep(20)


