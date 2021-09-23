import requests
from bs4 import BeautifulSoup

from scipy.stats import binom


class Function(object):
    # 引数のページ先のhtmlElementsをすべて返す
    @staticmethod
    def getAllElements(search_url):
        getPage = requests.get(search_url)
        htmlElements = BeautifulSoup(getPage.content, "html.parser")

        return htmlElements

    # 台一覧ページ(beautifulSoupObject)から台ごとのurlを取得して配列で返す
    @staticmethod
    def getMachineUrlList(beautifulSoupObj):
        machineUrlList = []
        elements = beautifulSoupObj.select("div.machine-graph-viewer > a")
        if not elements:
            print("[heroku][slot_scraping][getMachineUrlList]台一覧を取得できませでした。")

        for element in elements:
            machineUrlList.append(
                "https://store.p-ken.jp" + element.get('href'))

        return machineUrlList

    # データページ(beautifulSoupObject)からボーナスデータを取得する
    @staticmethod
    def getBonusData(beautifulSoupObj, bonusDataDict):
        try:

            # 台番号取得
            machineId = beautifulSoupObj.select_one(
                "div.result-header div.col > span").text
            machineId = machineId.replace(" ", "")
            machineId = machineId.replace(":", "")
            machineId = machineId.replace("台番号", "")

            bonusDataDict["id"] = machineId

            # BB,RB,BB確率,RB確率,合算,累計ゲーム数 を取得
            datalist = []
            bonusContents = beautifulSoupObj.select_one("div.inner-box")
            bonusElements = bonusContents.select("div.s4 > div")
            # BB,RB,BB確率,RB確率
            for bonusElement in bonusElements:
                data = bonusElement.text
                data = data.replace(" ", "")
                data = data.replace("\n", "")
                datalist.append(data)

            bonusDataDict["BB"] = datalist[1]
            bonusDataDict["RB"] = datalist[3]
            bonusDataDict["BB_ave"] = datalist[6]
            bonusDataDict["RB_ave"] = datalist[7]

            # 合算取得
            total_ave = bonusContents.select_one("div.total_hit_rate").text
            total_ave = total_ave.replace(" ", "")
            total_ave = total_ave.replace("\n", "")
            bonusDataDict["total_ave"] = datalist[7]

            # 累計取得
            elements = bonusContents.select("div.s12 > div.row > div")[2]
            total_game = elements.select("div")[1].text
            total_game = total_game.replace(" ", "")
            total_game = total_game.replace("\n", "")
            bonusDataDict["total_game"] = total_game

            return bonusDataDict

        except Exception as e:
            print('[heroku][slot_scraping][getBonusData]ゲームデータの取得に失敗しました。' + str(e))

    # 設定1~6までの設定期待度(%)を計算
    # 計算式参考url(https://note.com/kamaniwa/n/n6c4bc688d5b3)
    @staticmethod
    def setting_judgement(slot_info: dict, gameData: dict):
        try:
            # 設定1~6までの推定確率を計算
            for i in range(1, 7):

                # BBのみでの設定推測
                bb_guess_value = binom.pmf(
                    int(gameData["BB"]), int(gameData["total_game"]), 1.0 / float(slot_info["bb_probability" + str(i)]))
                bb_guess_value = '{:.4f}'.format(bb_guess_value)
                # RBのみでの設定推測
                rb_guess_value = binom.pmf(
                    int(gameData["RB"]), int(gameData["total_game"]), 1.0 / float(slot_info["rb_probability" + str(i)]))
                rb_guess_value = '{:.4f}'.format(rb_guess_value)

                # BB推定とRB推定から最終的な設定を推測する。
                total_guss_value = (float(bb_guess_value)
                                    * float(rb_guess_value))*100
                total_guss_value = '{:.4f}'.format(total_guss_value)
                total_guss_value = '{:.2f}'.format(
                    (float(total_guss_value) / 2.355) * 100)

                gameData["guess_class" + str(i)] = total_guss_value

            return gameData
        except Exception as e:
            print('[heroku][slot_scraping][setting_judgement]設定解析に失敗しました。' + str(e))
