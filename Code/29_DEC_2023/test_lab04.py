import time

from selenium import webdriver

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)


    time.sleep(5)

    #driver.close() # Close will close the current window(tab)
    # # It will not close the other tabs
    # # Session != null (Invalid)
    #time.sleep(200) # enable this otherwise python interpretator will close all window

    driver.quit()
    # Session == None
    # Close all the tabs(windows)
