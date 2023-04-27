import time
import random
from ..tools.metamask import metaMask
from ..tools.adspower import adsPower
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


from abc import ABC, abstractmethod

class BaseRunner(ABC):
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.meta_mask = metaMask(driver)

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def create_exchange(self):
        pass
    
    @abstractmethod
    def confirm_exchange(self):
        pass
    
    def quit(self):
        self.quit()
        self.meta_mask.quit()
    
    def close_enviroment(self):
        # 关闭所有tab页面，然后关闭打开的环境
        time.sleep(3.5)
        self.close_window()
        # self.ads_power.close_environment()
        random_int = random.randint(150, 230)
        time.sleep(random_int)
    
    def quit(self):
        self.driver.quit()

    def close_window(self):
        # 获取所有标签页的句柄
        all_handles = self.driver.window_handles
        # 循环切换到其他标签页并关闭
        for handle in all_handles:
            if handle != all_handles[0]:
                self.driver.switch_to.window(handle)
                self.driver.close()

        # 关闭浏览器
        self.driver.quit()









