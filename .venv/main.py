import config
from selenium import webdriver
import time

DEBUG = config.DEBUG


def scraping_exe():

    try:
        driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
        driver.get("https://www.google.com/")

        time.sleep(5)
    except Exception as e:
        print('ページアクセス時に例外が発生しました。' + str(e))
    driver.quit()


scraping_exe()
