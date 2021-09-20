import config
from selenium import webdriver
# driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
import time
from database.slot_information import SlotInformation

from Function import Function


def scraping_exe():

    try:

        # スクレイピング先を取得
        slotInformation = SlotInformation()
        slot_infos = slotInformation.getAll()

        for slot_info in slot_infos:

            search_url = slot_info["search_url"]

            time.sleep(2)

            topPagehtmlElements = Function.getAllElements(search_url)
            machineUrlList = Function.getMachineUrlList(topPagehtmlElements)

    except Exception as e:
        print('[scraping_exe]失敗しました。' + str(e))


scraping_exe()
