import time

from selenium import webdriver

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Edge()
    driver.get("https://w8077.dev.xz98a.skf.io")
    time.sleep(2000)
    driver.quit()
