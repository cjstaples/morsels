# import multiprocessing
import threading
from multiprocessing.context import Process

from selenium import webdriver
import io
import sys
import os


def get_short_urls():
    # short_urls = ["https://stackoverflow.com","https://www.google.com/"]
    path = "./"
    # filename = "shorty_autoconsumer.csv"
    filename = "shorty_autoconsumer_sample.csv"
    pathname = path + filename
    short_urls = []

    print("using file:: " + str(pathname))
    file = open(pathname, "r")
    for line in file:
        input_url = str(line)
        # print("tmp:: " + str(input_url))
        short_urls.append(input_url)

    return short_urls


def open_page(driver, url="https://stackoverflow.com", entry=0):
    debug = False
    if debug:
        print('PID:: ', str(os.getpid()), '-- NOT opening url:: ' + url)
        # print('   pid:: ', str(os.getpid()))
    else:
        print('PID:: ', str(os.getpid()), ':: ENTRY:: ', entry, ':: URL:: ', url)
        driver.get(url)
        driver.implicitly_wait(5)
        save_page(driver)
        driver.quit()


def save_page(driver):
    html = driver.page_source
    with io.open(driver.title + ".html", "w", encoding="utf-8") as f:
        f.write(html)
        f.close()


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
    return driver


def do_sanity_multiprocess():
    names = ['A','B','C']
    procs = []
    # proc = Process(target=do_lite_function)
    # procs.append(proc)
    # proc.start()

    for count, name in enumerate(names, 1):
        print(count, name)
        proc = Process(target=do_lite_function, args=(name,))
        procs.append(proc)
        proc.start()


def do_cfg_multiprocess(processes=1):
    print('processes:: ', str(processes))
    procs = []
    for i in range(processes):
        print('_')
        print('_process #:: ', str(i))
        proc = Process(target=do_lite_function, args=(i,))
        procs.append(proc)
        proc.start()


def do_main_driver_multiprocess(processes=1,reps=1):
    print('processes:: ', str(processes))
    procs = []
    for i in range(processes):
        print('_')
        print('_process #:: ', str(i))
        proc = Process(target=main_driver, args=(reps,))
        procs.append(proc)
        proc.start()


def do_lite_function(param="D"):
    print('name:: '+str(param))
    pass


def main_driver(reps=1):
    short_urls = get_short_urls()
    print('main driver reps::',str(reps))
    for i in range(reps):
        for entry, url in enumerate(short_urls, 0):
            driver = setup_driver()
            url = "http://s.egft.in/" + url
            open_page(driver, url, entry)


def main():
    print('(pagesave) main:')
    print('')

    number_of_instances = 3
    # print("SHORTURLS:: " + str(short_urls))
    # do_sanity_multiprocess()
    # do_cfg_multiprocess(number_of_instances)
    do_main_driver_multiprocess(number_of_instances)

    # main_driver()

    print('')
    print('(pagesave) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()

    # print("Number of cpu : ", multiprocessing.cpu_count())

    sys.exit(result)
