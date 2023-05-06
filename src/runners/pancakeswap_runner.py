import time
import random
from ..tools.metamask import metaMask
from ..tools.adspower import adsPower
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from ..projects.pancakeSwap import pancakeSwap
from .runner import BaseRunner

operate_line = {
    1: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    2: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    3: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    4: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    5: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    6: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    },
    7: {
        'token_pairs': ['ETH->USDC','ETH->USDC'],
        'platforms': []
    }
}

class pancakeSwapRunner(BaseRunner):
    def __init__(self, driver:webdriver.Chrome):
        super().__init__(driver)
        # self.ads_power = adsPower(serial_number)
        # self.random_eth_value = random_eth_value
        # self.driver = self.ads_power.open_environment()
        # self.driver = driver
        self.pancakeSwap = pancakeSwap(driver)
        # self.meta_mask = metaMask(driver)

    def run(self, from_token, to_token, value):
        # driver = self.ads_power.open_environment()
        # sync_swap = syncSwap(driver)

        # self.create_exchange('ETH', 'WBTC','random')
        # time.sleep(2)
        # self.confirm_exchange()

        exchange_value = self.create_exchange(from_token, to_token,value)
        # self.create_exchange('WBTC', 'ETH','100%')
        time.sleep(2)
        self.confirm_exchange(from_token)
        # time.sleep(3)
        return exchange_value
        # self.close_enviroment()

    def switch_to_zksync_network(self):
        self.pancakeSwap.open_blank_tab()
        self.pancakeSwap.close_wallet_tabs()
        self.meta_mask.unlock_wallet()
        self.pancakeSwap.close_wallet_tabs()
        current_window = self.pancakeSwap.open_url("https://pancakeswap.finance/swap?chain=zkSync")
        self.driver.switch_to.window(current_window)
        time.sleep(2)
        self.pancakeSwap.switch_to_zksync_network()
        time.sleep(2)
        self.pancakeSwap.connect_metamask()
        time.sleep(3)
        self.meta_mask.connect_website()
        time.sleep(2)
        self.driver.switch_to.window(current_window)
        time.sleep(2)
    

    def create_exchange(self, from_token, to_token,value):
        self.pancakeSwap.open_url("https://pancakeswap.finance/swap?chain=zkSync")
        # is_zksync = self.sync_swap.is_zksync_network()
        # if not is_zksync:
        #     # 切换至小狐狸操作
        #     print('执行切换网络')
        #     self.meta_mask.connect_website()
        #     time.sleep(2)

        self.pancakeSwap.connect_metamask()
        time.sleep(3)

        # 切换至小狐狸操作
        self.meta_mask.connect_website()
        time.sleep(1)


        # 判断是否需要再次unlock成功，防止上一步并未成功
        self.pancakeSwap.try_unlock_wallet()

        # is_zksync = self.pancakeSwap.is_zksync_network()
        # if not is_zksync:
        #     # 切换至小狐狸操作
        #     print('执行切换网络')
        #     self.meta_mask.connect_website()
        #     time.sleep(1)

        # 选择交易对
        time.sleep(3)
        self.pancakeSwap.choose_exchange_pair(from_token, to_token)
        exchange_value = self.pancakeSwap.input_exchange_value(from_token, value)
        return exchange_value
    
    def confirm_exchange(self, from_token):
        try:
            time.sleep(2)
            is_nees_unlock = self.pancakeSwap.unlock_token(from_token)
            # time.sleep(2)
            if is_nees_unlock:
                self.meta_mask.approve_or_sign_or_confirm()
                # if self.pancakeSwap.is_operate_success():
                #     print('unlock_token成功')
                self.pancakeSwap.click_blank_area()
        except Exception as e:
            # 如果定位失败，执行其他逻辑或错误处理
            print(e)
            print("不需要Approve")

        # 确认交易
        time.sleep(7)
        self.pancakeSwap.swap()
        print('开始交易小狐狸确认')
        self.meta_mask.approve_or_sign_or_confirm()
        print('小狐狸确认执行成功')
        time.sleep(8)
        print('开始第二次交易小狐狸确认')
        self.meta_mask.approve_or_sign_or_confirm()
        print('小狐狸第二次确认执行成功')
        # if self.pancakeSwap.is_operate_success():
        #     print('swap_token成功')
        self.pancakeSwap.click_blank_area()
    








