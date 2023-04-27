
import pandas as pd
import msoffcrypto
import io
from config import global_config
from src.runners.pancakeswap_runner import pancakeSwapRunner
from src.tools.adspower import adsPower
from src.tools.excel import excel_decrypt, write_to_excel
from selenium.common.exceptions import NoSuchElementException
import random
import datetime as dt
import time

runner_list = {
    1: pancakeSwapRunner,
}


excute_path_list = {
    1:[{
        'from_token': 'ETH',
        'to_token': 'USDC',
        'value': 'random',
    },
    {
        'from_token': 'USDC',
        'to_token': 'ETH',
        'value': '100%',
    }],
}

# def excel_decrypt(file_path, password):
#     file = msoffcrypto.OfficeFile(open(file_path, "rb"))
#     file.load_key(password=password) # Use password
#     decrypted = io.BytesIO()
#     file.decrypt(decrypted)
#     pd.set_option('display.max_colwidth', None)
#     result = pd.read_excel(decrypted)
#     return result

# def write_to_excel(current_time, serial_number, address, isSuccess, exchange_value, duration, action, platform):
#     original_data = pd.read_excel('./data/output.xlsx')
#     input_line_data = {'time': [current_time],
#          'serial_number': [serial_number],
#          'address': [address],
#          'isSuccess': [isSuccess],
#          'duration': duration,
#          'action': action,
#          'value': [exchange_value],
#          'platform': platform
#         }
#     input_line_data = pd.DataFrame(input_line_data)
#     new_data = original_data.append(input_line_data)
#     new_data.to_excel('./data/output.xlsx', index=False)


def run_project(runner, from_token, to_token, value, is_last_step):
    print(type(runner).__name__)
    platform = type(runner).__name__
    print(from_token, '->', to_token, ',', 'value: ',value)
    current_time = dt.datetime.now().strftime('%F %T')
    start_time = time.time()
    exchange_value = runner.run(from_token,to_token,value)
    end_time = time.time()
    duration = end_time-start_time
    
    print("程序执行成功:", str(row['serial_number']), '，耗时', duration, '秒')
    time.sleep(5)
    # if is_last_step:
    #     runner.close_enviroment()
    return exchange_value
    # else:
    #     runner.quit()

# 读取加密的 Excel 文件（需要提供密码）
excel_path = global_config.get('path', 'account_path')
excel_passwd = global_config.get('config', 'excel_passwd')
result = excel_decrypt(file_path=excel_path, password=excel_passwd)
for index, row in result.iterrows():
    if row['serial_number'] in range(271,285):
        random_excute_path_index = random.randint(1, 1)
        excute_path = excute_path_list[random_excute_path_index]
        excute_path = [
            {
            'from_token': 'ETH',
            'to_token': 'USDC',
            'value': 'random',
        },
        {
            'from_token': 'USDC',
            'to_token': 'ETH',
            'value': '100%',
        }]

        ads_power = adsPower(str(row['serial_number']))
        driver = ads_power.open_environment()
        pancakeswap_runner = pancakeSwapRunner(driver)
        runner_list_new = {
            1: pancakeswap_runner,
        }
        
        for index, single_pair in enumerate(excute_path):
            runner = ''
            current_time = dt.datetime.now().strftime('%F %T')
            if index == 0:
                # 第一个默认打开syncswap, 网络切换至zksync
                print(str(row['serial_number']))
                pancakeswap_runner.switch_to_zksync_network()
            random_excute_runner_index = random.randint(1, 1)
            random_excute_runner_index = 1
            runner = runner_list_new[random_excute_runner_index]
            start_time = time.time()
            try: 
                is_last_step = (index == len(excute_path) - 1)
                exchange_value = run_project(runner, single_pair['from_token'], single_pair['to_token'], single_pair['value'], is_last_step)
                random_int = random.randint(30, 50)
                time.sleep(random_int)
                time.sleep(5)
                if index == len(excute_path) -1:
                    ads_power.close_environment()
                    end_time = time.time()
                    duration = end_time-start_time
            except Exception as e:
                # 处理捕获到的异常
                current_time = dt.datetime.now().strftime('%F %T')
                print("发生了异常:", str(row['serial_number']))
                print(e)
                end_time = time.time()
                duration = end_time-start_time
        random_int = random.randint(3, 10)
        time.sleep(random_int)