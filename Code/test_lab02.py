import time

from selenium import webdriver


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    Edge_Options = webdriver.EdgeOptions()
    # Give some extra argument or extension or anything to Chrome.
    # Chrome Options  - Chrome with the Extension, Window Size, Proxy, JS disabled or enable

    # extension_path = "C:\Users\GR4492.CORP\Downloads/adblocker.crx"
    # chrome_options.add_extension(extension_path)

    Edge_Options.add_argument("--start-maximized")
    #1. Headless Mode:Run Edge in headless mode (Without GUI)
    Edge_Options.add_argument("--headless=env")

    driver = webdriver.Chrome(options=Edge_Options)  # Fresh chrome which doesn't have anything
    driver.get("https://w8077.dev.xz98a.skf.io/")

    print(driver.title)
    time.sleep(5)
