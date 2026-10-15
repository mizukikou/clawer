# 匯入 requests 套件，負責發送網路請求
import requests

# 定義目標測試網址
url = "https://httpbin.org/get"

# 🎯【核心大腦：字典的值使用列表 List】
# 這裡模擬了電商網站的多選功能：
# 我們希望篩選 category（分類）同時包含 electronics（電子）與 books（書籍）
# 並且 on_sale（是否特價）必須為 true。
payload = {
    "category": ["electronics", "books"], # 💡 重點：用中括號 List 把多個條件包起來！
    "on_sale": "true"
}

# 📡【發送帶有列表參數的請求】
# 將 payload 傳入 params 參數。
# requests 套件在底層發現 "category" 的值是一個列表時，會非常聰明地自動將它拆開，
# 複製兩份欄位名稱，並用「&」符號串接起來！
res = requests.get(url, params=payload)

# 印出最終請求網址進行驗收
print(f"多值請求網址：{res.url}")

# 💡【最終輸出結果】：
# 程式執行後，您會看到網址自動變成了：
# https://httpbin.org
# 看到網址出現了兩個 category=... 了嗎？這就是標準的後端多選條件傳遞格式！
