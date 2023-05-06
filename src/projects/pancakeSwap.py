import time
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from .project import BaseProject

token_xpaths = {
    'ETH': '//div[text()="Ether"]',
    'USDC': '//div[text()="USD Coin"]',
    'USDT': '//div[text()="Tether USD"]',
    'WBTC': '//div[text()="Wrapped BTC"]',
    '100%': "//button[text()='Max']"
}

class pancakeSwap(BaseProject):
    def __init__(self, driver:webdriver.Chrome):
        super().__init__(driver)
        # self.driver = driver
        # self.current_window = self.driver.current_window_handle
        # self.actions = ActionChains(driver)
        
    def is_zksync_network(self):
        self.switch_to_current_window()
        time.sleep(3)
        # network_name = self.driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/nav/div[2]/div[4]/div/div[1]/div[2]/div[1]').text
        network_name = self.driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/nav/div[2]/div[5]/div/div[1]/div[2]/div[1]').text
        if network_name == 'zkSync Era':
            return True
        else:
            return False
    
        
    # 点击空白区域
    def click_blank_area(self):
        self.switch_to_current_window()
        time.sleep(1)
        # 将鼠标移动到页面的指定位置（这里以 (100, 100) 为示例）
        self.actions.move_by_offset(100, 100)
        # 点击空白区域
        self.actions.click()
        # 执行操作
        self.actions.perform()

    def try_unlock_wallet(self):
        time.sleep(2)
        self.switch_to_current_window()
        try_unlock_buttoms = self.driver.find_elements_by_xpath("//button[text()='Try unlock']")
        if len(try_unlock_buttoms) != 0:
                print("需要手动点击Try unlock连接钱包")
                try_unlock_buttom = try_unlock_buttoms[0]
                try_unlock_buttom.click()
                print("Try unlock成功")

    
    def switch_to_zksync_network(self):
        self.switch_to_current_window()
        Switch_to_zkSync_Era_buttoms = self.driver.find_elements_by_xpath("//button[text()='Switch to zkSync Era']")
        if len(Switch_to_zkSync_Era_buttoms) != 0:
            print("需要手动点击Switch to zkSync Era")
            Switch_to_zkSync_Era_buttom = Switch_to_zkSync_Era_buttoms[0]
            Switch_to_zkSync_Era_buttom.click()
            print("准备小狐狸确认切换网络")
    
    def connect_metamask(self):
        self.switch_to_current_window()
        time.sleep(3)
        # Connect_Wallet_buttoms = self.driver.find_elements_by_xpath("//button[text()='Connect Wallet']")
        Connect_Wallet_buttoms = self.driver.find_elements_by_xpath("//div[text()='Connect Wallet']")
        # print(111111111)
        if len(Connect_Wallet_buttoms) != 0 :
            print('Connect Wallet')
            Connect_Wallet_buttom = Connect_Wallet_buttoms[0]
            Connect_Wallet_buttom.click()
            time.sleep(3)
        choose_metamask_buttoms = self.driver.find_elements_by_css_selector('img[src="https://assets.pancakeswap.finance/web/wallets/metamask.png"]')
        if len(choose_metamask_buttoms) != 0 :
            print('Choose Metamask')
            choose_metamask_buttom = choose_metamask_buttoms[0]
            choose_metamask_buttom.click()
            time.sleep(3)

    def choose_exchange_pair(self, from_token, to_token):
        self.switch_to_current_window()
        pair = self.driver.find_elements_by_xpath('//*[@id="pair"]')
        from_token_select_element = pair[0]
        from_token_balance = self.driver.find_element_by_xpath('//*[@id="swap-currency-input"]/div[1]/div[2]')
        # line_1_pair_element.click()
        print('原始的from_token_select_element: ',from_token_select_element.text, ' 余额：', from_token_balance.text)
        to_token_select_element = pair[1]
        to_token_balance = self.driver.find_element_by_xpath('//*[@id="swap-currency-output"]/div[1]/div[2]')
        print('原始的to_token_select_element: ', to_token_select_element.text, ' 余额：', to_token_balance.text)
        
        if (from_token_select_element.text == from_token):
            print('目前from_token已经是',from_token, '不需要重复选择')
        else:
            time.sleep(2)
            from_token_select_element.click()
            time.sleep(2)
            token_input_element = self.driver.find_element_by_id('token-search-input')
            
            token_input_element.send_keys(from_token)
            time.sleep(2)
            print(token_xpaths[from_token])
            # from_token_element = self.driver.find_element_by_xpath(token_xpaths[from_token]) if from_token == 'ETH' else self.driver.find_element_by_css_selector(token_xpaths[from_token])
            from_token_element = self.driver.find_element_by_xpath(token_xpaths[from_token])
            time.sleep(2)
            from_token_element.click()
            time.sleep(2)
        if (to_token_select_element.text == to_token):
            print('目前to_token已经是',to_token, '不需要重复选择')
        else:
            time.sleep(2)
            to_token_select_element.click()
            time.sleep(2)
            token_input_element = self.driver.find_element_by_id('token-search-input')
            token_input_element.send_keys(to_token)
            time.sleep(2)
            print(token_xpaths[from_token])
            # to_token_element = self.driver.find_element_by_xpath(token_xpaths[to_token]) if to_token == 'ETH' else self.driver.find_element_by_css_selector(token_xpaths[to_token])
            to_token_element = self.driver.find_element_by_xpath(token_xpaths[to_token])
            time.sleep(2)
            to_token_element.click()

    
    def approve_token(self, token):
        # approve_buttom_text = 'Approve ' + token
        # print("//button[text()='Approve {}']".format(token))
        unlock_erc20_token_buttom = self.driver.find_element_by_xpath("//button[text()='Approve']")
        unlock_erc20_token_buttom.click()
        time.sleep(5)
        # self.click_blank_area()

    def input_exchange_value(self,from_token, value):
        self.switch_to_current_window()
        pair = self.driver.find_elements_by_xpath('//*[@id="pair"]')
        from_token_select_element = pair[0]
        from_token_balance = self.driver.find_element_by_xpath('//*[@id="swap-currency-input"]/div[1]/div[2]')
        from_token_balance = float(from_token_balance.text.split(' ')[1])
        print('原始的from_token: ',from_token_select_element.text, ' 余额：', from_token_balance)
        if from_token == 'ETH':
            print('ETH->TOKEN')
            time.sleep(1)
            random_input_value = round(random.uniform((from_token_balance - 0.002)*0.3, from_token_balance - 0.002), 6)
            print('random_input_value:', random_input_value)
            eth_input_element = self.driver.find_element_by_xpath('//*[@id="swap-currency-input"]/div[2]/label/div[1]/input')
            eth_input_element.send_keys(str(random_input_value))
            time.sleep(3)
            # return {'token':from_token, 'value':eth_input_element}
            return eth_input_element
        else:
            print('TOKEN->ETH')
            time.sleep(2)
            amount_buttom = self.driver.find_element_by_xpath(token_xpaths[value])
            amount_buttom.click()
            time.sleep(3)
            # return {'token':from_token, 'value':from_token_balance}
            return from_token_balance
    
    def unlock_token(self, token):
        self.switch_to_current_window()
        unlock_erc20_token_buttoms = self.driver.find_elements_by_xpath("//button[text()='Enable {}']".format(token))
        if len(unlock_erc20_token_buttoms):
            print('需要解锁erc20 Token')
            current_window_handles = self.driver.window_handles
            unlock_erc20_token_buttom = unlock_erc20_token_buttoms[0]
            unlock_erc20_token_buttom.click()
            time.sleep(2)
            # 最多重试两次
            i = 0
            while len(self.driver.window_handles) == len(current_window_handles) and i < 2:
                print('小狐狸没有弹出来，再试一次，', '第', i, '次')
                # unlock_erc20_token_buttoms = self.driver.find_elements_by_xpath('//*[@id="swap-box"]/div[1]/div/div[3]/button')
                # if len(unlock_erc20_token_buttoms):
                #     unlock_erc20_token_buttom = unlock_erc20_token_buttoms[0]
                #     unlock_erc20_token_buttom.click()
                i += 1
                time.sleep(1.5)
            return True
        else:
            print('不需要解锁erc20 Token')
            return False
        # self.click_blank_area()

    def swap(self):
        print('开始执行交易')
        self.switch_to_current_window()
        swap_buttoms = self.driver.find_elements_by_xpath("//button[text()='Swap']")
        if len(swap_buttoms):
            print('找到Swap按钮')
            swap_buttom = swap_buttoms[0]
            swap_buttom.click()
        time.sleep(1.5)
        # Accept
        accept_buttoms = self.driver.find_elements_by_xpath("//button[text()='Accept']")
        if len(accept_buttoms):
            accept_buttom = accept_buttoms[0]
            accept_buttom.click()
        
        confirm_swap_buttoms = self.driver.find_elements_by_xpath("//button[text()='Confirm Swap']")
        if len(confirm_swap_buttoms):
            confirm_swap_buttom = confirm_swap_buttoms[0]
            confirm_swap_buttom.click()
        
        time.sleep(5)
        # self.click_blank_area()
            
        