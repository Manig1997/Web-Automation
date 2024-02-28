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
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "div[title='Folders'] div[class='aw-tile-iconContainer aw-layout-flexColumn sw-justify-center']"))
    )

    #Search button
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys("*")
    search_button = driver.find_element(By.XPATH, "//span[@aria-label='Search']//span[@class='aw-icon']//*[name()='svg']")
    search_button.click()

    WebDriverWait(driver, 25).until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='aw-in-content-search-box aw-search-searchBox'] div[class='sw-search-iconContainer']")))

    more_option = driver.find_element(By.XPATH, "//a[@aria-label='More...'][1]")
    more_option.click()

    category_list = driver.find_element(By.XPATH, "(//div[@class='sw-section sw-section-content sw-column'])[2]")
    print(category_list.text)

    time.sleep(10)
