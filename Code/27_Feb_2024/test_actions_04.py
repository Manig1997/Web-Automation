import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


def test_actions_04():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    #iframe = driver.find_element(By.TAG_NAME,'iframe')
    #ActionChains(driver).scroll_to_element(iframe).perform()
    #scroll from element with offset 0,-50
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    scroll_origin= ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()


    time.sleep(20)
