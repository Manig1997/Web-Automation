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

    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "div[title='Folders'] div[class='aw-tile-iconContainer aw-layout-flexColumn sw-justify-center']"))
    )
    # time.sleep(40)
    # Folder box
    folder_box = driver.find_element(By.XPATH, "//div[@data-locator='tile-container-Awp0HomeFolderTile']")
    folder_box.click()

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[id='gridView_row12_col2'] div[class='aw-splm-tableCellTop']")))

    # right hand side "New" option
    new_option = driver.find_element(By.XPATH, "//button[@aria-label='New']")
    new_option.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li[aria-label='Create Change']")))

    # Add option
    create_Change_option = driver.find_element(By.XPATH, "//li[@aria-label='Create Change']")
    create_Change_option.click()

    # selecting SKF change notice option
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[title='SKF Change Notice']")))

    SKF_change_notice_option = driver.find_element(By.XPATH, "//div[@title='SKF Change Notice']")
    SKF_change_notice_option.click()

    # validation of creation window
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class='propertyLabelTopContainer'] span[class='sw-property-name']")))
    ECN_no = driver.find_elements(By.XPATH, "//div[@class='aw-widgets-propertylabel']")
    for i in ECN_no:
        if i.text == 'ECN-"nnnnnn"':
            print(i.text)
        # list_results = driver.find_elements(By.XPATH, "//span[@role='heading']")
        # for i in list_results:
        #   print(i.text)
           #time.sleep(20)
