import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.positive
def test_open_login():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Edge()
    driver.get("https://mpm-test.dev.xz98a.skf.io/")
    driver.maximize_window()

    WebDriverWait(driver, 40).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".aw-layout-locationTitle"), "Teamcenter")
    )

    # Profile button
    profile = driver.find_element(By.CSS_SELECTOR, "[class='sw-avatar-name sw-avatar-initials']")
    profile.click()

    time.sleep(5)
    # WebDriverWait(driver, 10).until(
    # EC.visibility_of_element_located((By.XPATH, "//span[@iconid='uiDock']")
    # ))

    # Roles expand
    roles_expand = driver.find_element(By.XPATH, "//button[@title='Pop Out User Properties']")
    roles_expand.click()
    time.sleep(5)

    # Changing different role

    roles_expand_02 = driver.find_element(By.XPATH, "//a[normalize-space()='Manufacturing.D-Factory.Gothenburg.SKF']")
    roles_expand_02.click()
    time.sleep(5)

    role_change = driver.find_element(By.XPATH, "//span[normalize-space()='Purchasing.D-Factory.Gothenburg.SKF']")
    role_change.click()
    time.sleep(10)

    validation = driver.find_element(By.XPATH, "//a[normalize-space()='Purchasing.D-Factory.Gothenburg.SKF']")

    print(validation.text)
    time.sleep(10)
