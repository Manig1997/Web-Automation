import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
@pytest.mark.positive
def test_open_login():
    driver = webdriver.Edge()
    driver.get("https://mpm-test.dev.xz98a.skf.io")
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='100 %'")
    WebDriverWait(driver, 40).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".aw-layout-locationTitle"), "Teamcenter")
    )

    #Search button
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys("*")
    search_button = driver.find_element(By.XPATH, "//span[@aria-label='Search']//span[@class='aw-icon']//*[name()='svg']")
    search_button.click()

    WebDriverWait(driver, 25).until(
       EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='aw-in-content-search-box aw-search-searchBox'] div[class='sw-search-iconContainer']"), "Category")
    )
    #search = driver.find_element(By.XPATH, "//div[@title='Category']")
    #print(search.text)
    #heading_element = driver.find_element(By.XPATH, "//div[@title='Category']")
    #assert heading_element.text == os.getenv("Category")
    #time.sleep(10)
