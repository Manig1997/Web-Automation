import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_actions_03():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")


    # clickable = driver.find_element(By.ID, "clickable")
    # ActionChains(driver)\
    # .double_click(clickable)\
    # .perform()
    # Backslash is use for continues
    #hoverable = driver.find_element(By.ID, "hover")
    #ActionChains(driver) \
     #   .move_to_element(hoverable) \
      #  .perform()
    draggable =driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(draggable,droppable).perform()

    time.sleep(20)
