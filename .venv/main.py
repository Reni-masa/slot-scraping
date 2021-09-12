from selenium import webdriver

DRIVER_PATH = './tools/chromedriver'

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
