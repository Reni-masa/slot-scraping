import requests
from bs4 import BeautifulSoup


class Function(object):
    # 引数のページ先のhtmlElementsをすべて返す
    @staticmethod
    def getAllElements(search_url):
        getPage = requests.get(search_url)
        htmlElements = BeautifulSoup(getPage.content, "html.parser")

        return htmlElements

    @staticmethod
    # 台一覧ページ(beautifulSoupObjct)から台ごとのurlを取得して配列で返す
    def getMachineUrlList(beautifulSoupObj):
        machineUrlList = []
        elements = beautifulSoupObj.select("div.machine-graph-viewe > a")
        if not elements:
            print("[heroku][getMachineUrlList]台一覧を取得できませでした。")

        for element in elements:
            machineUrlList.append("https:" + element.get('href'))

        return machineUrlList
