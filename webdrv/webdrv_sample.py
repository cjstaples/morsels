#  webdriver sample
#  messing around with options
#  e.g.
#
#

import sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def submall_validation(driver, submall):
    validation_data = {
        "is_valid": None,
        "header_logo": None,
        "url_displayed": None
    }

    image_src = driver.find_element(by=By.CLASS_NAME, value='header-logo__image').get_attribute('src')
    if submall in image_src:
        validation_data["is_valid"] = True
        validation_data["header_logo"] = image_src
    else:
        validation_data["is_valid"] = False
    print(validation_data)
    return validation_data


def main():
    print('(webdrv) main:')
    print()

    # todo: any user input
    #

    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    submall = None
    driver.get("http://www.google.com")
    # submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    submall = ""
    driver.get("https://kroger-gcm.semi.cashstar.com/")
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    submall = "bakersplus"
    driver.get("https://kroger-gcm.semi.cashstar.com/bakersplus")
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    submall = "city-market"
    driver.get("https://kroger-gcm.semi.cashstar.com/city-market")
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    submall = "dillons"
    driver.get("https://kroger-gcm.semi.cashstar.com/dillons")
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    submall = "kroger"
    driver.get("https://kroger-gcm.semi.cashstar.com/kroger")
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    driver.quit()

    print()
    print('(webdrv) end::')

    return 0


def webdrv_logic(case):
    output = ''

    # simplistic, but handle both true without dealing with multi line issue
    if check_fizz(case) & check_buzz(case):
        output = 'FizzBuzz'
    # only fizz true
    elif check_fizz(case):
        output = 'Fizz'
    # only buzz true
    elif check_buzz(case):
        output = 'Buzz'
    # neither true
    else:
        output = case

    return output


def check_buzz(case):
    check = False
    if (case % 5) == 0:
        check = True
    return check


def check_fizz(case):
    check = False
    if (case % 3) == 0:
        check = True
    return check


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
