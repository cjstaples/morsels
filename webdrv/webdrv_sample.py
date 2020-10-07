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
    import pathlib
    from urllib.parse import urlparse

    validation_data = {
        "submall": submall,
        "is_valid": None,
        "header_logo_src": None,
        "header_logo_path": None,
        "url_tried": "TBA",
        "url_displayed": None
    }

    logo_src = driver.find_element(by=By.CLASS_NAME, value='header-logo__image').get_attribute('src')
    logo_src_class = driver.find_element(by=By.CLASS_NAME, value='header-logo__image').get_attribute('src')

    # cashbot specific?
    # logo_src_css = driver.find(by=By.CSS_SELECTOR, value='a.header-logo img').get_attribute('src')

    logo_path = urlparse(logo_src).path
    submall_name = pathlib.Path(logo_path).stem

    url_displayed = driver.current_url

    validation_data["header_logo_src"] = logo_src
    validation_data["header_logo_path"] = logo_path
    validation_data["url_displayed"] = url_displayed

    if submall in logo_src:
        validation_data["is_valid"] = True
        validation_data["header_logo"] = logo_src
    else:
        validation_data["is_valid"] = False

    print(':: validation_data:')
    for key, value in validation_data.items():
        print('{k:>16}'.format(k=key), ' : ', '{v:>120}'.format(v=value))
    print('::::')

    return validation_data


def main():
    print('(webdrv) main:')
    print()

    urlbase = 'https://kroger-gcm.semi.cashstar.com'
    submalls = (
        '','bakersplus','city-market','dillons',
        'food-4-less','foods-co','fred-meyer','frys-food',
        'gerbes', 'jay-c-foods', 'king-soopers',
        'marianos', 'metro-market', 'owens-market', 'payless',
        'pick-n-save', 'qfc', 'ralphs', 'smiths',
        'kroger'
    )

    # todo: any user input
    #
    # service = Service('/usr/local/bin/chromedriver')
    # service.start()

    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(service.service_url)

    # submall = None
    # driver.get("http://www.google.com")
    # # submall_validation_data = submall_validation(driver, submall)
    # time.sleep(5)

    submall = ""
    driver.get(urlbase)
    submall_validation_data = submall_validation(driver, submall)
    time.sleep(5)

    for submall in submalls:
        url = urlbase + f'/{submall}'
        driver.get(url)
        submall_validation_data = submall_validation(driver, submall)
        time.sleep(3)


    # submall = "bakersplus"
    # driver.get("https://kroger-gcm.semi.cashstar.com/bakersplus")
    # submall_validation_data = submall_validation(driver, submall)
    # time.sleep(5)
    #
    # submall = "city-market"
    # driver.get("https://kroger-gcm.semi.cashstar.com/city-market")
    # submall_validation_data = submall_validation(driver, submall)
    # time.sleep(5)
    #
    # submall = "dillons"
    # driver.get("https://kroger-gcm.semi.cashstar.com/dillons")
    # submall_validation_data = submall_validation(driver, submall)
    # time.sleep(5)
    #
    # submall = "kroger"
    # driver.get("https://kroger-gcm.semi.cashstar.com/kroger")
    # submall_validation_data = submall_validation(driver, submall)
    # time.sleep(5)

    driver.quit()

    print()
    print('(webdrv) end::')

    return 0


def webdrv_logic(case):
    output = ''

    if check_romeo(case) & check_juliet(case):
        output = 'LOVE'
    else:
        output = case

    return output


def check_romeo(case):
    check = False
    return check


def check_juliet(case):
    check = False
    return check


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
