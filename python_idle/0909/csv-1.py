import csv
import os  # 1. 必須載入 os 模組才能檢查檔案是否存在

data = [
    {"品名": "台積電", "股價": 800, "評等": "買進"},
    {"品名": "聯發科", "股價": 1000, "評等": "持有"},
    {"品名": "鴻海", "股價": 150, "評等": "買進"}
]

file_name = "stocks.csv"
fieldnames = ["品名", "股價", "評等"]  # 提早定義，確保後面都能使用

# ===【模擬部分 A：若檔案不存在就先建立並寫入初始資料】===
if not os.path.exists(file_name):
    with open(file_name, mode='w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"檔案 {file_name} 不存在，已成功初始化並儲存。")


# ===【修正後的新增資料邏輯】===
new_data = [
    {"品名": "新產品X", "股價": 500, "評等": "觀察"}
]

# 2. 修正拼字 Ture -> True
file_exist = False
if os.path.exists(file_name):
    file_exist = True  
    
    # 3. 修正 open 語法：明確加上 encoding=，並將結尾補回 as f
    with open(file_name, mode='a', encoding='utf-8-sig', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 續寫（mode='a'）時不需要寫入標題（writeheader），直接寫入資料即可
        writer.writerows(new_data)
    print("新資料已成功追加到檔案末尾。")

    
# ==================== 部分 B：讀取資料 ====================
with open(file_name, mode='r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    print("\n從 CSV 讀取回來的内容：")
    for row in reader:
        # 由於股價讀出來是字串，靠右對齊可以用 :>8
        print(f"品名：{row['品名']:　<8} | 股價：{row['股價']:>8} | 評等：{row['評等']:　<8}")
