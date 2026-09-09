import csv
import os  # 1. 必須載入 os 模組才能檢查檔案是否存在

def write_data(file_name,fieldnames,data):
    # ===【模擬部分 A：若檔案不存在就先建立並寫入初始資料】===
    if not os.path.exists(file_name):
        with open(file_name, mode='w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"檔案 {file_name} 不存在，已成功初始化並儲存。")
        
def append_data(file_name,fieldnames):
  # ===【改用 input 的動態新增資料邏輯】===
    print("\n--- 請輸入新股票資料 ---")
    input_name = input("請輸入品名（例如：新產品X）：")
    input_price = int(input("請輸入股價（例如：500）："))
    input_rating = input("請輸入評等（例如：觀察）：")
    # 將輸入的資料組合呈您的結構：[ {"品名": "...", "股價": "...", "評等": "..."} ]
    new_data = [
        {
            "品名": input_name, 
            "股價": input_price, 
            "評等": input_rating
        }
    ]
  
    file_exist = False
    if os.path.exists(file_name):
        file_exist = True  
        
        # 3. 修正 open 語法：明確加上 encoding=，並將結尾補回 as f
        with open(file_name, mode='a', encoding='utf-8-sig', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            # 續寫（mode='a'）時不需要寫入標題（writeheader），直接寫入資料即可
            writer.writerows(new_data)
        print("新資料已成功追加到檔案末尾。")
        
def read_data(file_name):    
    # ==================== 部分 B：讀取資料 ====================
    with open(file_name, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        #headers = reader.fieldnames
        print("\n從 CSV 讀取回來的内容：")
        for row in reader:
            # 由於股價讀出來是字串，靠右對齊可以用 :>8
            print(f"品名：{row['品名']:　<8} | 股價：{row['股價']:>8} | 評等：{row['評等']:　<8}")
            #列表推導式 output = " | ".join([f"{h}：{row[h]:<8}" for h in headers])
            # print(output)
data = [
    {"品名": "台積電", "股價": 800, "評等": "買進"},
    {"品名": "聯發科", "股價": 1000, "評等": "持有"},
    {"品名": "鴻海", "股價": 150, "評等": "買進"}
]

file_name = "stocks.csv"
fieldnames = ["品名", "股價", "評等"]  # 提早定義，確保後面都能使用
write_data(file_name,fieldnames,data)
read_data(file_name)

# # ===【修正後的新增資料邏輯】===
# new_data = [
#     {"品名": "新產品X", "股價": 500, "評等": "觀察"}
# ]

while True:
    append_data(file_name,fieldnames)
    read_data(file_name)
    cont = input("是否繼續新增資料？(y/n)：")
    if cont.lower() != 'y':
        break



