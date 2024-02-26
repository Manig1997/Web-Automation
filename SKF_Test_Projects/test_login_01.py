import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login():
    driver = webdriver.Edge()
    driver.get("https://mpm-test.dev.xz98a.skf.io")
    driver.maximize_window()
    time.sleep(40)

