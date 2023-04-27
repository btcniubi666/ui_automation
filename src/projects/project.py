import time
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from abc import ABC, abstractmethod

class BaseProject(ABC):
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.current_window = self.driver.current_window_handle
        self.actions = ActionChains(driver)

    def close_wallet_tabs(self):
        all_handles = self.driver.window_handles
        # # 检查是否是空白标签页
        print(all_handles)
        # 循环切换到其他标签页并关闭
        for handle in all_handles:
            print(handle)
            self.driver.switch_to.window(handle)
            time.sleep(1.5)
            current_url = self.driver.current_url
            if not (self.driver.current_url == 'about:blank' or self.driver.title.isdigit()):
                # print('关闭')
                self.driver.close()
            time.sleep(1)
        all_handles_new = self.driver.window_handles
        for handle in all_handles_new:
            self.driver.switch_to.window(handle)
            if self.driver.title.isdigit():
                break
        
    def switch_to_current_window(self):
        time.sleep(3)
        self.driver.switch_to.window(self.current_window)
        

    def open_url(self,website):
        time.sleep(1)
        self.driver.get(website)
        time.sleep(2)
        current_window = self.driver.current_window_handle
        self.driver.switch_to.window(current_window)
        self.current_window = current_window
        print(self.driver.title)
        return current_window
    
    def switch_to_zksync_network(self):
        pass
    
    @abstractmethod
    def connect_metamask(self):
        pass

    @abstractmethod
    def choose_exchange_pair(self):
        pass
    
    def approve_token(self):
        pass

    def input_exchange_value(self,from_token, value):
        pass
    
    def unlock_token(self, token):
        pass

    @abstractmethod
    def swap(self):
        pass

    def open_blank_tab(self):
        # 打开一个新的空白页
        self.driver.execute_script("window.open('');")
        
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
            
        