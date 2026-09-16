# 1. 定義原始資料清單 (Raw Data List)
# 資料包含三個主要問題：資料重複、價格含有符號($,)、缺失值呈現為字串 "None"
raw_data = [
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPhone 15", "price": "$29,900"},  # 重複資料
    {"item": "iPad Air", "price": "$19,500"},
    {"item": "MacBook", "price": "None"}        # 缺失值
]

# 2. 初始化用來存放清洗後資料的空清單
cleaned_data = []

# 3. 初始化一個集合 (Set) 用來記錄已經處理過的資料，達到「去重」的目的
# 集合的特性是元素不會重複，查詢速度極快
seen = set()

# 4. 開始使用 for 迴圈逐一存取原始清單中的每一筆資料 (字典型態)
for data in raw_data:
    
    # 💡 步驟 A：檢查並剔除重複資料
    # 將字典的 key 與 value 轉成不可變的 tuple，因為集合(set)只能存放不可變的物件
    data_tuple = (data["item"], data["price"])
    
    if data_tuple in seen:
        continue  # 如果這個資料組合已經出現過，立刻「跳過本次迴圈」，不放入新清單
    
    # 如果是第一次見到的新資料，就加入集合中記錄起來
    seen.add(data_tuple)
    
    # 💡 步驟 B：欄位清理與資料轉型
    price_str = data["price"]  # 取出價格字串
    
    # 狀況一：處理特殊的缺失值
    if price_str == "None":
        price = None  # 將文字字串 "None" 轉型為 Python 真正的空值物件 None
        
    # 狀況二：處理正常帶有符號的價格字串
    else:
        # 1. 使用 .replace("$", "") 移除金錢記號
        # 2. 使用 .replace(",", "") 移除千分位逗號
        # 3. 使用 int() 將清理乾淨的數字字串（例如 "29900"）強制轉型為「整數」
        price = int(price_str.replace("$", "").replace(",", ""))
        
    # 💡 步驟 C：建立乾淨的字典並歸檔
    # 組裝成資料型態正確、且沒有重複的新字典，並附加到乾淨的清單中
    cleaned_data.append({
        "item": data["item"], 
        "price": price
    })

# 5. 印出最後清洗完成的結果
print("--- 清洗後的乾淨資料 ---")
print(cleaned_data)
