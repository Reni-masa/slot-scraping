# .env ファイルをロードして環境変数へ反映
import os
from dotenv import load_dotenv
load_dotenv()

# 実行環境判別用変数
DEBUG = os.getenv("DEBUG")

CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')

# heroku DB(mysql)接続情報
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_USERNAME = os.getenv('DB_USERNAME')
