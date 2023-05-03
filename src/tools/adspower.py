import time
from selenium import webdriver
import requests,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

class adsPower:
    def __init__(self, serial_number):
        self.ads_id = serial_number
        self.open_url = "http://local.adspower.com:50325/api/v1/browser/start?serial_number=" + serial_number
        self.close_url = "http://local.adspower.com:50325/api/v1/browser/stop?serial_number=" + serial_number
    
    def open_environment(self):
        resp = requests.get(self.open_url).json()
        print(resp)
        if resp["code"] != 0:
            print(resp["msg"])
            print("please check serial_number")
            sys.exit()
        chrome_driver = resp["data"]["webdriver"]
        print(chrome_driver)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
        try:
            driver.maximize_window()
        except:
            print('窗口已经最大化')
        time.sleep(3)
        return driver
    def close_environment(self):
        resp = requests.get(self.close_url)