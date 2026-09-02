# 載入操作系統相關功能的模組（用於檢查路徑、建立資料夾、處理檔名）
import os
# 載入高階檔案操作模組（用於複製檔案並保留詳細屬性）
import shutil
# 從 datetime 模組中載入 datetime 類別（用於獲取系統當前時間）
from datetime import datetime

# 定義一個名為 backup_file 的函式，接收兩個參數：來源檔案路徑、目標備份資料夾路徑
def backup_file(source_file, target_folder):

    # 檢查來源檔案是否「不存在」
    if not os.path.exists(source_file):
        # 若找不到檔案，印出錯誤訊息提示使用者
        print(f"錯誤：找不到來源檔案 '{source_file}'")
        # 直接結束函式，不執行後續的備份動作
        return
    
    # 檢查目標備份資料夾是否「不存在」
    if not os.path.exists(target_folder):
        # 若不存在，自動建立該資料夾（makedirs 可連同多層父資料夾一起建立）
        os.makedirs(target_folder)
        # 印出提示訊息，通知已建立新資料夾
        print(f"建立新資料夾：{target_folder}")
        
    # 使用 try-except 結構來捕捉備份過程中可能發生的非預期錯誤（例如檔案被佔用、權限不足）
    try:
        # 產生時間戳記檔名（例如：20260413_1530_data.csv）
        
        # 取得目前系統時間，並格式化為「年月日_時分」的字串（例如 "20260902_0923"）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        
        # 從完整的路徑中切出「純檔名與副檔名」（例如把 "C:/docs/data.csv" 變成 "data.csv"）
        file_name = os.path.basename(source_file)
        
        # 使用 F-string 將時間戳記與純檔名用底線組合，形成新的備份檔名
        new_file_name = f"{timestamp}_{file_name}"
        
        # 組合完整的目標路徑
        # 將目標資料夾路徑與新檔名結合（例如 "my_backups/20260902_0923_data.csv"）
        destination = os.path.join(target_folder, new_file_name)
        
        # 執行檔案複製。copy2 會連同檔案的修改時間、權限等元數據（Metadata）一起複製
        shutil.copy2(source_file, destination) # 執行複製
        
        # 印出成功訊息，並顯示檔案實際儲存的完整路徑
        print(f"備份成功！檔案已存至：{destination}")

    # 若 try 區塊內的程式碼發生任何異常，則跳至此處執行
    except Exception as e:
        # 印出錯誤原因，避免程式直接崩潰中斷
        print(f"備份過程中發生未知錯誤：{e}")

# 呼叫函式：嘗試將當前目錄下的 "config.ini" 備份到 "my_backups" 資料夾中
backup_file("config.ini", "my_backups")

# (路徑前的 r 可以防止反斜線 \ 造成程式碼解讀錯誤)
# src_file = r"C:\Users\User\Documents\Default.rdp"
