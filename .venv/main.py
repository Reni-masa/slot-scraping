import config
from selenium import webdriver
# driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
import time
from database.Slot_information import SlotInformation

from Function import Function


def scraping_exe():

    try:

        # マスタ機種情報を取得
        slotInformation = SlotInformation()
        slot_infos = slotInformation.getAll()

        # for slot_info in slot_infos:

        #     search_url = slot_info["search_url"]

        #     time.sleep(2)

        #     topPageHtmlElements = Function.getAllElements(search_url)
        #     machineUrlList = Function.getMachineUrlList(topPageHtmlElements)

        #     for machineUrl in machineUrlList:
        #         dataPageHtmlElements = Function.getAllElements(machineUrl)
        #         # 登録データ定義
        #         bonusDataDict = {
        #             "id": None,
        #             "BB": 0,
        #             "RB": 0,
        #             "BB_ave": 0,
        #             "RB_ave": 0,
        #             "total_game": 0,
        #             "total_ave": 0,
        #             "guess_class1": 0,
        #             "guess_class2": 0,
        #             "guess_class3": 0,
        #             "guess_class4": 0,
        #             "guess_class5": 0,
        #             "guess_class6": 0,
        #         }
        #         # 当日データ取得
        #         bonusDataDict = Function.getBonusData(
        #             dataPageHtmlElements, bonusDataDict)

        #         # 台番号取得できなかったらスキップ
        #         if not bonusDataDict['id']:
        #             continue

        #         # 設定判別
        #         bonusDataDict = Function.setting_judgement(
        #             slot_info, bonusDataDict)

        # デバッグここから
        slot_info = slot_infos[0]

        dataPageHtmlElements = Function.getAllElements(
            "https://store.p-ken.jp/p-kingkankosakaewakamiya/bonus/details/751/2/0/")

        bonusDataDict = {
            "id": None,
            "BB": 0,
            "RB": 0,
            "BB_ave": 0,
            "RB_ave": 0,
            "total_game": 0,
            "total_ave": 0,
            "guess_class1": 0,
            "guess_class2": 0,
            "guess_class3": 0,
            "guess_class4": 0,
            "guess_class5": 0,
            "guess_class6": 0,
        }
        bonusDataDict = Function.getBonusData(
            dataPageHtmlElements, bonusDataDict)

        # 設定判別
        bonusDataDict = Function.setting_judgement(
            slot_info, bonusDataDict)

        # ここまで
    except Exception as e:
        print('[heroku][slot_scraping][scraping_exe]失敗しました。' + str(e))


scraping_exe()
