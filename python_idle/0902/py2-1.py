# 載入 Python 內建的 CSV 檔案處理模組
import csv

# 準備一組資料，結構為「清單 (List) 裡面包著字典 (Dictionary)」
# 每個字典代表一列（一行）資料，欄位名稱（Key）與內容值（Value）成對出現
data = [
    {"品名": "台積電", "股價": 800, "評等": "買進"},
    {"品名": "聯發科", "股價": 1000, "評等": "持有"},
    {"品名": "鴻海", "股價": 150, "評等": "買進"}
]

# 設定要產生的 CSV 檔案名稱（這裡會保存在程式碼執行的同一個資料夾下）
file_name = "stocks.csv"


# ==================== 部分 A：儲存資料 (寫入) ====================

# 使用 with open 語法安全地開啟檔案。當這個區塊結束時，Python 會自動關閉檔案，釋放資源
# mode='w'        -> 代表寫入模式（Write），如果檔案已存在會被覆蓋
# encoding='utf-8-sig' -> 加上 -sig 會在檔案開頭加入 BOM 標記，能防止 Windows Excel 打開時中文變亂碼
# newline=''      -> 這是必加參數！防止 Windows 系統在寫入 CSV 時，每一行中間自動多跑出一個空白橫行 (\n 造成的)
with open(file_name, mode='w', encoding='utf-8-sig', newline='') as f:
    
    # 定義 CSV 檔案最頂端的第一行標題（欄位名稱），順序必須與你想輸出的順序一致
    fieldnames = ["品名", "股價", "評等"]
    
    # 建立一個「字典專用的 CSV 寫入器 (DictWriter)」
    # 它會自動幫我們比對 data 裡面字典的 Key 是否符合 fieldnames 定義的欄位
    # 左邊的 fieldnames：是 csv.DictWriter 工具內建的「參數名稱」。右邊的 fieldnames：是自己定義的「變數名稱」（可以自由改名）。
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # 執行動作：將 fieldnames 定義的標題（"品名", "股價", "評等"）寫入檔案的第一行
    writer.writeheader()
    
    # 執行動作：將 data 清單內所有的字典資料，一次性全部整批寫入檔案中
    writer.writerows(data)

# 當程式離開 with 區塊後，檔案已安全關閉。印出提示訊息告知使用者
print(f"檔案 {file_name} 已成功儲存。")


# ==================== 部分 B：讀取資料 ====================

# 再次開啟同一個檔案，準備讀取裡面的內容
# mode='r'        -> 代表唯讀模式（Read）
# encoding='utf-8-sig' -> 必須使用與寫入時相同的編碼，才能正確解析出中文字
with open(file_name, mode='r', encoding='utf-8-sig') as f:
    
    # 建立一個「字典專用的 CSV 讀取器 (DictReader)」
    # 它會自動把 CSV 的第一行當作欄位名稱（Key），之後的每一行資料都會被轉換成一個字典
    reader = csv.DictReader(f)
    
    # 印出裝飾文字（\n 代表在文字開頭先換一行，排版比較好看）
    print("\n從 CSV 讀取回來的内容：")
    
    # 使用 for 迴圈，逐行讀取檔案內容
    # 每一次迴圈中的 row 變數，都是一個代表該行資料的字典（例如：{"品名": "台積電", "股價": "800", ...}）
    for row in reader:
        # 使用 F-string 格式化輸出
        # 💡 注意：row['品名'] 括號內要用單引號，以便和最外層的雙引號區隔，避免語法報錯
        print(f"品名：{row['品名']:　<8} | 股價：{row['股價']:8}| 評等：{row['評等']:　<8}")
        # :　<8：代表當字串不足 8 個字元寬度時，在右邊補全形空白（靠左對齊）。
        # 如果指定了填補字元（例如全形空白），就必須同時指定對齊方向（如 < 靠左、> 靠右或 ^ 置中）
