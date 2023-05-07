import pandas as pd
import msoffcrypto
import io

def excel_decrypt(file_path, password):
    file = msoffcrypto.OfficeFile(open(file_path, "rb"))
    file.load_key(password=password) # Use password
    decrypted = io.BytesIO()
    file.decrypt(decrypted)
    pd.set_option('display.max_colwidth', None)
    result = pd.read_excel(decrypted)
    return result

def write_to_excel(current_time, serial_number, address, isSuccess, exchange_value, duration, action, platform):
    original_data = pd.read_excel('./data/output.xlsx')
    input_line_data = {'time': [current_time],
         'serial_number': [serial_number],
         'address': [address],
         'isSuccess': [isSuccess],
         'duration': duration,
         'action': action,
         'value': [exchange_value],
         'platform': platform
        }
    input_line_data = pd.DataFrame(input_line_data)
    new_data = original_data.append(input_line_data)
    new_data.to_excel('./data/output.xlsx', index=False)