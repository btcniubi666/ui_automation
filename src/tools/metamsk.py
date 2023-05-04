import time
from selenium import webdriver
from config import global_config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
class metaMask:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.current_window = driver.current_window_handle
        # self.actions = ActionChains(driver)
    
    def is_window_open(self, window_handle):
        return window_handle in self.driver.window_handles
    
    def switch_to_current_window(self):
        time.sleep(7)
        window_handles = self.driver.window_handles
        self.current_window = window_handles[-1]
        self.driver.switch_to.window(window_handles[-1])
        print('当前窗口名: ', self.driver.title)
        print('当前窗口url: ', self.driver.current_url)
        # 如果切换的倒数第一个窗口不是Braavos窗口，则执行一下遍历操作，直至切换正确
        if self.driver.title != 'MetaMask Notification':
            for handle in window_handles:
                self.driver.switch_to.window(handle)
                time.sleep(1)
                if self.driver.title == 'MetaMask Notification':
                    self.current_window = handle
                    break
        time.sleep(2)
        if self.driver.title == 'MetaMask Notification':
            return True
        else:
            return False
    
    def switch_to_self_window(self):
        print('准备切换窗口')
        time.sleep(7)
        window_handles = self.driver.window_handles
        print('窗口列表：', window_handles)
        self.current_window = window_handles[-1]
        print('准备切换至弹出的窗口：', window_handles[-1])
        self.driver.switch_to.window(window_handles[-1])
        time.sleep(2.5)
        print('当前窗口名: ', self.driver.title)
        print('当前窗口url: ', self.driver.current_url)
        # 如果切换的倒数第一个窗口不是Braavos窗口，则执行一下遍历操作，直至切换正确
        if self.driver.title != 'MetaMask Notification':
            for handle in window_handles:
                self.driver.switch_to.window(handle)
                time.sleep(1.5)
                if self.driver.title == 'MetaMask Notification':
                    self.current_window = handle
                    break
        time.sleep(2)
        if self.driver.title == 'MetaMask Notification':
            return True
        else:
            return False
    
    def open_url(self,website):
        time.sleep(1)
        self.driver.get(website)
        # self.driver.execute_script("window.open('{0}', '_blank');".format(website))
        time.sleep(2)
        window_handles = self.driver.window_handles
        self.current_window = window_handles[-1]
        self.driver.switch_to.window(window_handles[-1])
        # current_window = self.driver.current_window_handle
        # self.driver.switch_to.window(current_window)
        # self.current_window = current_window
        print(self.driver.title)
        return self.current_window
    
    def unlock_wallet(self):
        is_open = self.switch_to_current_window()
        self.open_url('chrome-extension://gdkpiamecifeaiiggfgbofjgehlpjhhi/home.html#onboarding/welcome')
        print(self.driver.title)
        print(is_open)
        # if not is_open:
        #     return
        time.sleep(2)
        if self.is_window_open(self.current_window):
            passwd_buttoms = self.driver.find_elements_by_xpath('//*[@id="password"]')
            if len(passwd_buttoms) != 0:
                print("输入密码")
                metamask_passwd = global_config.get('config', 'metamask_passwd')
                passwd_buttom = passwd_buttoms[0]
                passwd_buttom.send_keys(metamask_passwd)
            time.sleep(1)
        if self.is_window_open(self.current_window):
            unlock_buttoms = self.driver.find_elements_by_xpath("//button[text()='Unlock']")
            if len(unlock_buttoms) != 0:
                print("解锁钱包")
                unlock_buttom = unlock_buttoms[0]
                unlock_buttom.click()
            time.sleep(2)
        

    def connect_website(self):
        is_open = self.switch_to_current_window()
        print(self.driver.title)
        if not is_open:
            return
        time.sleep(2)
        if self.is_window_open(self.current_window):
            passwd_buttoms = self.driver.find_elements_by_xpath('//*[@id="password"]')
            if len(passwd_buttoms) != 0:
                print("输入密码")
                metamask_passwd = global_config.get('config', 'metamask_passwd')
                passwd_buttom = passwd_buttoms[0]
                passwd_buttom.send_keys(metamask_passwd)
            time.sleep(1)
        if self.is_window_open(self.current_window):
            unlock_buttoms = self.driver.find_elements_by_xpath("//button[text()='Unlock']")
            if len(unlock_buttoms) != 0:
                print("解锁钱包")
                unlock_buttom = unlock_buttoms[0]
                unlock_buttom.click()
            time.sleep(2)
        if self.is_window_open(self.current_window):
            next_buttoms = self.driver.find_elements_by_xpath("//button[text()='Next']")
            if len(next_buttoms) != 0:
                print("下一步")
                next_buttom = next_buttoms[0]
                next_buttom.click()
            time.sleep(1)
        if self.is_window_open(self.current_window):
            connect_buttoms = self.driver.find_elements_by_xpath("//button[text()='Connect']")
            if len(connect_buttoms) != 0:
                print("连接网站")
                connect_buttom = connect_buttoms[0]
                connect_buttom.click()
        # 判断是否需要有添加网络的这一步，有的话就执行添加，没有就跳过
        time.sleep(2.5)
        if self.is_window_open(self.current_window):
            approve_buttoms = self.driver.find_elements_by_xpath("//button[text()='Approve']")
            if len(approve_buttoms) != 0:
                print("添加网路")
                approve_buttom = approve_buttoms[0]
                self.scroll_down(approve_buttom)
                approve_buttom.click()
            time.sleep(1)
        if self.is_window_open(self.current_window):
            switch_networ_buttoms = self.driver.find_elements_by_xpath("//button[text()='Switch network']")
            if len(switch_networ_buttoms) != 0:
                print("切换网络")
                switch_networ_buttom = switch_networ_buttoms[0]
                switch_networ_buttom.click()
        
        if self.is_window_open(self.current_window):
            sign_buttoms = self.driver.find_elements_by_xpath("//button[text()='Sign']")
            if len(sign_buttoms) != 0:
                print("切换网络")
                sign_buttom = sign_buttoms[0]
                sign_buttom.click()


    def confirm(self):
        if self.driver.title != 'MetaMask Notification':
            self.switch_to_current_window()
            print(self.driver.title)
        time.sleep(2)
        edit_gas_buttoms = self.driver.find_elements_by_xpath("//button[text()='Edit']")
        site_suggested_buttoms = self.driver.find_elements_by_xpath("//span[text()='Site suggested']")
        advance_bottoms = self.driver.find_elements_by_xpath("//span[text()='Advanced']")
        Market_bottoms = self.driver.find_elements_by_xpath("//span[text()='Market']")
        if len(edit_gas_buttoms) != 0 and len(advance_bottoms) == 0:
            print("编辑gas")
            edit_buttom = edit_gas_buttoms[0]
            edit_buttom.click()

            time.sleep(1)
            edit_suggested_gas_buttoms = self.driver.find_element_by_xpath("//button[text()='Edit suggested gas fee']")
            edit_suggested_gas_buttoms.click()
            time.sleep(1)
            gas_limit_input_element = self.driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/div[2]/div/div[2]/div[1]/div/div[1]/label/div[2]/input')
            time.sleep(1)
            random_int = random.randint(1400000, 1600000)
            if int(gas_limit_input_element.get_attribute('value')) > 1400000:
                gas_limit_input_element.send_keys(Keys.CONTROL + "a")  # 选中所有内容
                gas_limit_input_element.send_keys(Keys.BACKSPACE)  # 删除内容
                gas_limit_input_element.send_keys(str(random_int))  # 输入新的内容
                time.sleep(1.5)
            save_buttom = self.driver.find_element_by_xpath("//button[text()='Save']")
            save_buttom.click()
            time.sleep(3)
            gas_fee_show = self.driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/h6[1]/div/div/span[2]')
            print("gas_fee_show:",gas_fee_show.text)
            # confirm_buttom = self.driver.find_element_by_xpath("//button[text()='Confirm']")
            # time.sleep(1)
            # confirm_buttom.click()
        if len(site_suggested_buttoms) != 0 or len(advance_bottoms) != 0:
            print("编辑网站gas")
            if (len(site_suggested_buttoms) != 0):
                site_suggested_buttom = site_suggested_buttoms[0]
                site_suggested_buttom.click()
            else:
                advance_bottom = advance_bottom[0]
                advance_bottom.click()
            # else:
            #     Market_buttom = Market_bottoms[0]
            #     Market_buttom.click()
            time.sleep(2)
            # data-testid="edit-gas-fee-item-custom"
            advance_bottom = self.driver.find_element_by_xpath("//span[text()='⚙️']")
            advance_bottom.click()
            time.sleep(2)
            Edit_bottom = self.driver.find_element_by_xpath("//a[text()='Edit']")
            Edit_bottom.click()
            time.sleep(1.5)
            gas_limit_input_element = self.driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/div[2]/div/div[3]/label/div[2]/input')
            time.sleep(1)
            random_int = random.randint(1400000, 1600000)
            if int(gas_limit_input_element.get_attribute('value')) > 1400000:
                gas_limit_input_element.send_keys(Keys.CONTROL + "a")  # 选中所有内容
                gas_limit_input_element.send_keys(Keys.BACKSPACE)  # 删除内容
                gas_limit_input_element.send_keys(str(random_int))  # 输入新的内容
                time.sleep(1.5)
            save_buttom = self.driver.find_element_by_xpath("//button[text()='Save']")
            save_buttom.click()
            time.sleep(3)
            gas_fee_show = self.driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/h6[1]/div/div/span[2]')
            print("gas_fee_show:",gas_fee_show.text)
        # if len(Market_bottoms) != 0:
        #     Market_buttom = Market_bottoms[0]
        #     Market_buttom.click()
        #     time.sleep(2)
        #     Edit_bottom = self.driver.find_element_by_xpath("//a[text()='Edit']")
        #     Edit_bottom.click()
        #     time.sleep(1.5)
        #     gas_limit_input_element = self.driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/div[2]/div/div[3]/label/div[2]/input')
        #     time.sleep(1)
        #     random_int = random.randint(1400000, 1600000)
        #     if int(gas_limit_input_element.get_attribute('value')) > 1400000:
        #         gas_limit_input_element.send_keys(Keys.CONTROL + "a")  # 选中所有内容
        #         gas_limit_input_element.send_keys(Keys.BACKSPACE)  # 删除内容
        #         gas_limit_input_element.send_keys(str(random_int))  # 输入新的内容
        #         time.sleep(1.5)
        #     save_buttom = self.driver.find_element_by_xpath("//button[text()='Save']")
        #     save_buttom.click()
        #     time.sleep(3)
        #     gas_fee_show = self.driver.find_element_by_xpath('//*[@id="app-content"]/div/div/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div/h6[1]/div/div/span[2]')
        #     print("gas_fee_show:",gas_fee_show.text)
            
        confirm_buttom = self.driver.find_element_by_xpath("//button[text()='Confirm']")
        time.sleep(1)
        confirm_buttom.click()
        # if self.is_window_open(self.current_window):
            # edit_gas_buttoms = None
            # edit_gas_buttoms = self.driver.find_elements_by_xpath("//button[text()='Edit']")
            # edit_gas_buttoms_2 = self.driver.find_elements_by_xpath("//button[text()='EDIT']")
            # if (len(edit_gas_buttoms_1)):
            #     edit_gas_buttoms = edit_gas_buttoms_1
            # if (len(edit_gas_buttoms_1)):
            #     edit_gas_buttoms = edit_gas_buttoms_2

            # 编辑gas，有两种界面，一种是小狐狸的默认界面，一种是网站推荐界面，需要分两种类型进行操作
            

    def quit(self):
        self.driver.quit()
    
    def approve(self):
        if self.driver.title != 'MetaMask Notification':
            self.switch_to_current_window()
            print(self.driver.title)
        time.sleep(2)
        if self.is_window_open(self.current_window):
            # use_default_buttoms = self.driver.find_elements_by_xpath("//button[text()='Use default']")
            use_default_buttoms = self.driver.find_elements_by_xpath("//button[text()='Max']")
            if len(use_default_buttoms) != 0:
                print("设置授权金额")
                use_default_buttom = use_default_buttoms[0]
                use_default_buttom.click()
        time.sleep(1)
        if self.is_window_open(self.current_window):
            next_buttoms = self.driver.find_elements_by_xpath("//button[text()='Next']")
            if len(next_buttoms) != 0:
                print("下一步")
                next_buttom = next_buttoms[0]
                next_buttom.click()
            time.sleep(1)
        time.sleep(3)
        approve_buttom = self.driver.find_element_by_xpath("//button[text()='Approve']")
        time.sleep(1)
        approve_buttom.click()
    
    def sign(self):
        if self.driver.title != 'MetaMask Notification':
            self.switch_to_current_window()
            print(self.driver.title)
        print(self.driver.title)
        time.sleep(2)
        sign_buttoms = self.driver.find_elements_by_xpath("//button[text()='Sign']")
        # 使用JavaScript代码将元素滚动到可视区域
        if len(sign_buttoms):
            self.scroll_down(sign_buttoms[0])
        # 定位到向下滚动箭头图标元素
        down_arrow_element = self.driver.find_element(By.CLASS_NAME, "fa-arrow-down")
        down_arrow_element.click()
        time.sleep(2)
        sign_buttom = sign_buttoms[0]
        sign_buttom.click()
    
    def approve_or_sign_or_confirm(self):
        # self.switch_to_self_window()
        is_open = self.switch_to_current_window()
        print('已执行切换至小狐狸操作，当前窗口：',self.driver.title)
        if not is_open:
            return
        print('小狐狸切换操作执行完成，当前窗口：', self.driver.title)
        print('当前tab: ',self.driver.title)
        # time.sleep(7)
        reject_buttoms = self.driver.find_elements_by_xpath("//button[text()='Reject']")
        # 等待小狐狸可以操作
        i = 0
        while len(reject_buttoms) == 0 and i < 5:
            time.sleep(1)
            print('狐狸还不能操作', '第', i, '次')
            reject_buttoms = self.driver.find_elements_by_xpath("//button[text()='Reject']")
            time.sleep(1.5)
            i += 1
        time.sleep(2)
        reject_buttoms = self.driver.find_elements_by_xpath("//button[text()='Reject']")
        if len(reject_buttoms):
            self.scroll_down(reject_buttoms[0])
        approve_buttoms = self.driver.find_elements_by_xpath("//button[text()='Use default']")
        use_max_buttoms = self.driver.find_elements_by_xpath("//button[text()='Max']")
        if (len(approve_buttoms) or len(use_max_buttoms)):
            print('Metamask执行approve操作')
            self.approve()
        sign_buttoms = self.driver.find_elements_by_xpath("//button[text()='Sign']")
        if (len(sign_buttoms)):
            print('Metamask执行sign操作')
            self.sign()
        confirm_buttoms = self.driver.find_elements_by_xpath("//button[text()='Confirm']")
        if (len(confirm_buttoms)):
            print('Metamask执行confirm操作')
            self.confirm()
    
    def scroll_down(self, element):
        # 执行 JavaScript 代码来向下滚动页面
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    