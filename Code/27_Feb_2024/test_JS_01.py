import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)


    time.sleep(20)
