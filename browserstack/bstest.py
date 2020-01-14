# browserstack basic test script
# https://www.browserstack.com/automate/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 8 Plus',
 'realMobile': 'true',
 'os_version': '11'
}

driver = webdriver.Remote(
    command_executor='http://chuckstaples1:h8sWEzyq8YhbdfppyYrU@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()
