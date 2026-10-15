# 匯入 requests 套件，負責處理發送 HTTP 網路請求
import requests

# 定義目標測試網址
url = "https://httpbin.org/get"

# 🎯【核心觀察：打包帶有空值的參數字典】
payload = {
    "q": "iphone",      # 正常有值的參數：關鍵字搜尋 iphone
    
    "min_price": None,  # 💡 狀況 A：設定為 Python 的 None（代表完全沒有這個東西）
                        # 核心特性：requests 看到 None，會直接在網址中「完全蒸發、直接忽略」這個欄位。
                        
    "max_price": ""     # 💡 狀況 B：設定為空字串 ""（代表有這個欄位，但內容是空的）
                        # 核心特性：requests 會保留這個鍵（Key），但在網址中讓它的值保持空白。
}

# 📡【發送帶有參數的請求】
res = requests.get(url, params=payload)

# 印出最終請求網址進行驗收
print(f"處理後的網址：{res.url}")

# 💡【最終輸出結果】：
# 程式執行後，您會看到終端機輸出的網址自動變成了：
# https://httpbin.org
#
# 🕵️ 偵探時間：
# 1. 欄位 "min_price" 徹底消失了！因為設定為 None，requests 貼心地幫你把它濾掉了。
# 2. 欄位 "max_price=" 被留下來了，但是等號後面什麼都沒接。因為它是空字串 ""。
