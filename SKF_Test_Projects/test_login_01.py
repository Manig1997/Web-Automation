import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_open_login():
    driver = webdriver.Edge()
    driver.get("https://mpm-test.dev.xz98a.skf.io")
    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[title='Folders'] div[class='aw-tile-iconContainer aw-layout-flexColumn sw-justify-center']"))
    )
    folder_box = driver.find_element(By.XPATH, "//div[@data-locator='tile-container-Awp0HomeFolderTile']")
    print(folder_box.text)
