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
    create_change_option = driver.find_element(By.XPATH, "//li[@aria-label='Create Change']")
    create_change_option.click()

    # selecting SKF change notice option
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[title='SKF Change Notice']")))

    skf_change_notice_option = driver.find_element(By.XPATH, "//div[@title='SKF Change Notice']")
    skf_change_notice_option.click()

    # validation of creation window
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class='propertyLabelTopContainer'] span[class='sw-property-name']")))

    ecn_no = driver.find_element(By.XPATH,"//form[@class='aw-layout-panelContent']//label[1]")
    print(ecn_no.text)

    revision = driver.find_element(By.XPATH, "//form[@class='aw-layout-panelContent']//label[2]")
    print(revision.text)

    synopsis = driver.find_element(By.NAME, "object_name")
    synopsis.send_keys("XXX")

    description = driver.find_element(By.NAME, "object_desc")
    description.send_keys("XXX")

    change_type_lov = driver.find_element(By.XPATH, "//input[@aria-label='CN Change Type']")
    change_type_lov.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "li[aria-label='General'] div[class='sw-aria-border aw-widgets-cellListItem aw-widgets-cellTop']")))

    list_options = driver.find_elements(By.XPATH,"(//ul[@role='listbox'])[9]/li")
    for list in list_options:
        print(list.text)

    change_sub_type_lov = driver.find_element(By.XPATH, "//input[@aria-label='Change Sub Type']")
    change_sub_type_lov.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > div:nth-child(1)")))

    list_options_02 = driver.find_elements(By.XPATH, "(//ul[@role='listbox'])[9]/li")
    for list in list_options_02:
        print(list.text)

    attachments = driver.find_element(By.XPATH,"//details[@caption='Attachments']//div[@class='sw-row']")
    print(attachments.text)

    open_new_change= driver.find_element(By.XPATH,"//span[@class='sw-property-name'][normalize-space()='Open New Change']")
    print(open_new_change.text)

    set_as_active_change = driver.find_element(By.XPATH,"//span[@class='sw-property-name'][normalize-space()='Set as Active Change']")
    print(set_as_active_change.text)

    click_option = driver.find_element(By.XPATH, "//div[@class='aw-panel-footer sw-row flex-wrap sw-column']//button[1]")
    print(click_option.text)

    click_and_submit_option = driver.find_element(By.XPATH,
                                       "//div[@class='sw-row h-9 aw-layout-nowrap aw-layout-subLocation afx-content-background']//button[2]")
    print(click_and_submit_option .text)

    time.sleep(20)
