import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_actions_01():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME, "firstname")

    #create object of Action Chain Class
    actions = ActionChains(driver)
    #Send keys but with shift
    actions\
        .key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name,"mani g")\
        .key_up(Keys.SHIFT).perform()

    url =driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    actions.context_click(url).perform()

    time.sleep(20)


