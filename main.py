import config
from selenium import webdriver
# driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
import time
from database.Slot_information import SlotInformation
from database.Slot_game_data import SlotGameData

from Function import Function
import datetime


def scraping_exe():

    try:
        today = datetime.date.today()

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
                # 登録データ定義
                bonusDataDict = {
                    "id": None,
                    "BB": 0,
                    "RB": 0,
                    "BB_ave": 0,
                    "RB_ave": 0,
                    "total_game": 0,
                    "total_ave": 0,
                    "class": 0,
                    "data_time": today,
                    "user_id": 1,
                    "store_id": 1,
                    "slot_id": slot_info["id"],
                    "guess_class1": 0,
                    "guess_class2": 0,
                    "guess_class3": 0,
                    "guess_class4": 0,
                    "guess_class5": 0,
                    "guess_class6": 0,
                }

                # 当日データ取得
                bonusDataDict = Function.getBonusData(
                    dataPageHtmlElements, bonusDataDict)

                # 台番号取得できなかったらスキップ
                if not bonusDataDict['id']:
                    continue

                # 設定判別
                bonusDataDict = Function.setting_judgement(
                    slot_info, bonusDataDict)

                # データベース登録
                slotGameData = SlotGameData()
                slotGameData.insertSlotGameData(slot_info["id"], bonusDataDict)

    except Exception as e:
        print('[heroku][slot_scraping][scraping_exe]失敗しました。' + str(e))


scraping_exe()
