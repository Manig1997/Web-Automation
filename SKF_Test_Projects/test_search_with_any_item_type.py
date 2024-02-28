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
    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      "div[title='Folders'] div[class='aw-tile-iconContainer aw-layout-flexColumn sw-justify-center']"))
                                    )

    # Search button
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys("MCN_000*")
    search_button = driver.find_element(By.XPATH,
                                        "//span[@aria-label='Search']//span[@class='aw-icon']//*[name()='svg']")
    search_button.click()

    WebDriverWait(driver, 25).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "li:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(2) div:nth-child(2) label:nth-child(1)")))

    list_of_search_items= driver.find_elements(By.XPATH, "//div[@class='aw-base-scrollPanel'][1]/ul/li")
    for list in list_of_search_items:
        print(list.text)

    time.sleep(10)
