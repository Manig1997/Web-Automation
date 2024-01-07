#


# Verify that the dashboard is loaded--> Pytest
# Create a Report to send to QA Lead--HTML-->Allure Report



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the browser
    # Navigate to a URL
    # Command--driver.get (Navigate command to Existing session)

    driver.get("https://app.vwo.com/")

    # Find the email Web Element and put email iD = "9952192457"
    # Find thw password input box and enter the password=Mpm@12345

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.ID, "login-password")
    signin_button_ele = driver.find_element(By.ID, "js-login-btn")

    # sending the data email and password and clicking on the button
    # send keys and click()

    email_address_ele.send_keys("manigs1997@gmail.com")
    password_ele.send_keys("Mpm@12345*")
    signin_button_ele.click()

    # There is a delay for 2-3 sec for this use below code
    time.sleep(5)
    LOGGER.info("title is"+driver.title)
    assert "Dashboard" in driver.title
