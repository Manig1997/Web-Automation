# create a file with name .gitignore
# git add .
# If showing diff git repository then type .git
#git init
# git add .
#git commit -m "FOlder name"
# git push
# git remote add origin https://github.com/Manig1997/Web-Automation.git >> It will vary depending upon the new folder creation
# git push
#git push --set-upstream origin master
# pip list>> gives you the versio of package installed inside the pycharm





#Selenium Web automation with Python
#Install the Import Lib
-Selenium ( > 4))
-Pytest
-Allure Pytest
-Pytest HTML
-xdist - Run Parallel Execution
-logging - Logging (API lib)
-Openpyxl - CSV,Excel
-Faker lib( Fake data generation)**
#pip install selenium pytest pytest-html allure-pytest

#How to Push the Git
#git add .
#git commit -m "Message"
#git push
#git pull ( if You have added somehting on github.com)

#how to get the html and allure report
pytest -s -v path>> report
pytest -s -v Code/6_Jan_2024/test01_vwologin.py --html=report.html 
pytest -s -v Code/6_Jan_2024/test01_vwologin.py--alluredir=./a llure-reports

# dot env
#pip install python-dotenv

#syntex for Frequent wait

#import os
#from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException) 

#ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    #wait = WebDriverWait(driver, 40, poll_frequency=1, ignored_exceptions=ignore_list)
    #element = EC.presence_of_element_located((By.CSS_SELECTOR,".aw-layout-locationTitle"))