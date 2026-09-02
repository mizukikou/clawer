import os
import shutil
import glob

# 1. 設定來源與目標資料夾路徑
source_dir = r"C:\venv_spider\python_idle\0902\my_backups"
target_dir = r"C:\venv_spider\python_idle\0902\history_logs"

# 2. 如果目標資料夾不存在，自動建立它
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"已建立目標資料夾：{target_dir}")

# 3. 找出來源資料夾中所有以 .ini 結尾的檔案路徑
#    os.path.join(source_dir, "*.*") 會組合成 "C:\...\my_backups\*.ini"
ini_files = glob.glob(os.path.join(source_dir, "*.*"))

# 4. 執行循環，逐一處理找到的檔案
for file_path in ini_files:
    # 取得純檔案名稱（例如："20260902_0929_config.ini"）
    file_name = os.path.basename(file_path)
    
    # 組合出新的檔案名稱，在前面加上 "old_"（例如："old_20260902_0929_config.ini"）
    new_file_name = "old_" + file_name
    
    # 組合出目標檔案的完整路徑（例如："C:\...\history_logs\old_20260902_0929_config.ini"）
    destination_path = os.path.join(target_dir, new_file_name)
    
    # 使用 shutil.copy 進行複製（保留來源檔案，並在目標路徑建立改名後的新檔）
    shutil.copy(file_path, destination_path)
    print(f"已成功複製並改名：{file_name} -> {new_file_name}")

print("--- 所有檔案備份完成 ---")
