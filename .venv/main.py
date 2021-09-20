import config
from selenium import webdriver
# driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
import time
from database.slot_information import SlotInformation

from Function import Function


def scraping_exe():

    try:

        # マスタ機種情報を取得
        slotInformation = SlotInformation()
        slot_infos = slotInformation.getAll()

        for slot_info in slot_infos:

            search_url = slot_info["search_url"]

            time.sleep(2)

            topPageHtmlElements = Function.getAllElements(search_url)
            machineUrlList = Function.getMachineUrlList(topPageHtmlElements)

            for machineUrl in machineUrlList:
                dataPageHtmlElements = Function.getAllElements(machineUrl)
                # 登録データを取得
                bonusDataDict = Function.getBonusData(dataPageHtmlElements)

        # デバッグここから
        # dataPageHtmlElements = Function.getAllElements(
        #     "https://store.p-ken.jp/p-kingkankosakaewakamiya/bonus/details/745/2/0/")

        # bonusDataDict = Function.getBonusData(dataPageHtmlElements)
        # print(bonusDataDict)

        # ここまで
    except Exception as e:
        print('[heroku][slot_scraping][scraping_exe]失敗しました。' + str(e))


scraping_exe()
