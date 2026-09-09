import csv
import os

def write_data(file_name, fieldnames, data):
    """初始化檔案，若不存在則建立並寫入資料"""
    if not os.path.exists(file_name):
        with open(file_name, mode='w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"檔案 {file_name} 不存在，已成功初始化並儲存。")
    else:
        print(f"檔案 {file_name} 已存在，跳過初始化。")

def append_data(file_name, fieldnames, data):
    """追加資料，若檔案不存在會自動補上標題"""
    file_exists = os.path.exists(file_name)
    
    with open(file_name, mode='a', encoding='utf-8-sig', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 📌 關鍵改進：若檔案不存在，追加時必須先寫入標題
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)
    print("新資料已成功追加到檔案末尾。")

def read_data(file_name):
    """動態讀取並列印 CSV 內容"""
    if not os.path.exists(file_name):
        print(f"錯誤：找不到檔案 {file_name}")
        return
        
    with open(file_name, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # 📌 關鍵改進：動態取得欄位名稱，避免寫死
        headers = reader.fieldnames
        print(f"\n從 {file_name} 讀取回來的内容：")
        
        for row in reader:
            # 📌 自動適應所有欄位排版
            output = " | ".join([f"{h}：{row[h]:<8}" for h in headers])
            print(output)

# === 測試資料與主程式 ===
if __name__ == "__main__":
    init_data = [
        {"品名": "台積電", "股價": "800", "評等": "買進"},
        {"品名": "聯發科", "股價": "1000", "評等": "持有"},
        {"品名": "鴻海", "股價": "150", "評等": "買進"}
    ]
    
    file_name = "stocks.csv"
    fieldnames = ["品名", "股價", "評等"]

    # 執行測試
    write_data(file_name, fieldnames, init_data)
    read_data(file_name)

    new_data = [{"品名": "新產品X", "股價": "500", "評等": "觀察"}]
    append_data(file_name, fieldnames, new_data)
    read_data(file_name)
