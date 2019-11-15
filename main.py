import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import sys
import pychromecast
import yaml

SOURCE_POINT_BASE = 262
CAST_POINT_BASE = 195
CAST_STOP_POINT_BASE = 195
CAST_LIST_OFFSET = 57

# 設定ファイル読み込み
f = open("settings.yaml", "r")
settings =   yaml.load(f, Loader=yaml.SafeLoader)

options = ChromeOptions()

options.add_argument('--user-data-dir=' + settings["CHROME_PROFILE_PATH"])

excludeList = [
    'disable-background-networking',
    'disable-default-apps',
]
options.add_experimental_option('excludeSwitches', excludeList)

driver = Chrome(settings["CHROME_DRIVER_PATH"], options=options)
 
driver.get("https://www.google.co.jp")
driver.set_window_position(0,0) # ブラウザの位置を左上に固定
driver.set_window_size(700,700) # ブラウザのウィンドウサイズを固定

# Chrome cast 一覧取得
chromecasts = pychromecast.get_chromecasts()
cast_list = sorted([cc.device.friendly_name for cc in chromecasts])

# 0 origin index
cast_index = cast_list.index(sys.argv[1])

# メニューを開いてキャストを押す
pyautogui.click(684, 97, 1, 1, 'left')
pyautogui.click(357, 336, 1, 1, 'left')

# ソースを選択してデスクトップをキャストを選択
time.sleep(2)
source_point = SOURCE_POINT_BASE + CAST_LIST_OFFSET * (len(cast_list) - 1)
pyautogui.click(370, source_point, 1, 1, 'left')
pyautogui.click(363, 378, 1, 1, 'left')

# 指定したchrome cast を選択，全画面を指定，共有を選択
cast_point = CAST_POINT_BASE + (CAST_LIST_OFFSET * cast_index)
pyautogui.click(400, cast_point, 1, 1, 'left')
pyautogui.click(855, 624, 1, 1, 'left')
pyautogui.click(1197, 843, 1, 1, 'left')

# 終了処理
while(True):
    input_line = input().replace("\n","")
    if input_line == "q":
        pyautogui.click(684, 97, 1, 1, 'left')
        pyautogui.click(357, 336, 1, 1, 'left')
        time.sleep(1)
        cast_stop_point = CAST_STOP_POINT_BASE  + (CAST_LIST_OFFSET * cast_index)
        pyautogui.click(340, cast_stop_point, 1, 1, 'left')
        driver.quit()
        sys.exit(0)
